import datetime
from googletrans import Translator
from langid.langid import LanguageIdentifier, model
import math
import pandas as pd
import requests
import os

# NOT USING THIS ONE

# from langdetect import detect_langs
# from langdetect import detect

# for i, row in data.iterrows():
#     webpagelink = row['WebpageLink']
#     text = row['Text']
#     print ('WEBPAGELINK:', webpagelink, 'TEXT:', text)

#     print ('detect_langs:', detect_langs(text))
#     print ('detect:', detect(text))
#     print()


# NOT USING THIS ONE EITHER BECAUSE IT COMES FROM GOOGLE AND WE ALREADY HAVE ONE FROM GOOGLE
# def textblob_pred(inputText):
#     from textblob import TextBlob
#     output = TextBlob(inputText).detect_language()
#     confidence = ''
#     pred = output
#     return inputText, output, confidence, pred


def clean_source(data):
    data = data.drop_duplicates()
    data['Text'] = data['Text'].apply(lambda x: x.strip())
    return data


def create_folder(rootdir, folderName):

    has_results_folder = False

    for subdir, dirs, files in os.walk(rootdir):
        if 'results' in subdir:
            has_results_folder = True

    if has_results_folder == False:
        os.mkdir(rootdir+'results')

    return 'Results folder created.'


def clean_output(text):
    # This is necesary because Chinese has multiple specifications
    if len(text) > 2:
        return text[0:2]
    else:
        return text


def watson_pred(inputText):
    headers = {'Content-Type': 'text/plain',}
    params = (('version', '2018-05-01'),)
    response = requests.post('https://gateway.watsonplatform.net/language-translator/api/v3/identify', headers=headers, params=params, data=inputText.encode('utf-8'), auth=('apikey', 'oVYfUrJnOA6DfIpfmX1M1eToEXWqPeB7-JOKob3elgGp'))
    output = response.json()
    confidence = pd.DataFrame(response.json()['languages']).head(1)['confidence'][0]
    pred = pd.DataFrame(response.json()['languages']).head(1)['language'][0]
    return inputText, output, confidence, clean_output(pred)


def langid_pred(inputText):
    # https://github.com/saffsd/langid.py
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
    output = identifier.classify(inputText)    
    confidence = output[1]
    pred = output[0]
    return inputText, output, confidence, clean_output(pred)


def googletrans_pred(inputText):
    translator = Translator()    
    output = translator.detect(inputText)
    confidence = output.confidence
    pred = output.lang
    return inputText, output, confidence, clean_output(pred)


def run_model(inputFile, outputDirectory):
    start = datetime.datetime.now()
    print('start:', start)

    create_folder(outputDirectory, 'results')

    data = pd.read_csv(inputFile)
    data = clean_source(data)
    phrases_to_check = data['Text'].unique()
    print('phrases_to_check:', len(phrases_to_check))

    denormColumnList = ['Text',
                'Confidence1','Confidence2','Confidence3',
                'Pred1','Pred2','Pred3',
                'MasterPred', 'MasterPredSumConfidences'
                ]
    denormOutputDf = pd.DataFrame(columns = denormColumnList)

    normColumnList = ['Text','Confidence','Pred','Model']
    normOutputDf = pd.DataFrame(columns = normColumnList)

    i = 0
    print('At Row:', 1)
    for Text in phrases_to_check:
        
        i += 1
        if i % 25 == 0:
            print('At Row:', i)

        Input1, Output1, Confidence1, Pred1 = watson_pred(Text)
        normWorkingDF1 = pd.DataFrame([[Text, Confidence1, Pred1, 'Watson']], columns = normColumnList)
        
        Input2, Output2, Confidence2, Pred2 = langid_pred(Text)
        normWorkingDF2 = pd.DataFrame([[Text, Confidence2, Pred2, 'LangId']], columns = normColumnList)

        Input3, Output3, Confidence3, Pred3 = googletrans_pred(Text)
        normWorkingDF3 = pd.DataFrame([[Text, Confidence3, Pred3, 'Google']], columns = normColumnList)

        normWorkingDF = pd.concat([normWorkingDF1, normWorkingDF2, normWorkingDF3], sort=False)
        normOutputDf = pd.concat([normOutputDf, normWorkingDF], sort=False)

        MasterPred = normWorkingDF.sort_values('Confidence', ascending=False).groupby(['Text']).first().reset_index()['Pred'][0]
        MasterPredSumConfidences = normWorkingDF[normWorkingDF['Pred'] == MasterPred]['Confidence'].sum()
        
        denormWorkingDF = pd.DataFrame([[Text, 
                                Confidence1, Confidence2, Confidence3,
                                Pred1, Pred2, Pred3,
                                MasterPred, MasterPredSumConfidences
                                ]], columns = denormColumnList)
        denormOutputDf = pd.concat([denormOutputDf, denormWorkingDF], sort=False)
        
    end = datetime.datetime.now()
    print('end:', end)

    id_list = data[['WebpageLink','ExpectedLanguage']].drop_duplicates().sort_values(by=['WebpageLink','ExpectedLanguage']) \
    .reset_index(drop=True).reset_index(drop=False) \
    .rename(index=str, columns={'index': 'PageId'})
    id_list['PageId'] = id_list['PageId'].apply(lambda x: str(x+1).zfill(5))
    combined_data = id_list.merge(data, left_on=['WebpageLink','ExpectedLanguage'], right_on=['WebpageLink','ExpectedLanguage'], how='left')
    combined_data = combined_data.merge(denormOutputDf, left_on='Text', right_on='Text', how='left')

    pred_cnt = combined_data.groupby(['PageId','WebpageLink','ExpectedLanguage','MasterPred'])['MasterPredSumConfidences'] \
    .agg(['count']).reset_index().rename(index=str, columns={'count': 'PredCnt'})
    total_cnt = combined_data.groupby(['PageId','WebpageLink','ExpectedLanguage'])['MasterPredSumConfidences'].agg(['count']).reset_index().rename(index=str, columns={'count': 'TotalCnt'})
    merged_data = pred_cnt.merge(total_cnt, left_on=['PageId','WebpageLink','ExpectedLanguage'], right_on=['PageId','WebpageLink','ExpectedLanguage'] , how='outer')
    merged_data['% Page'] = merged_data['PredCnt']/merged_data['TotalCnt']

    summary_norm = merged_data.pivot_table(index=['PageId','WebpageLink','ExpectedLanguage'], columns='MasterPred',values='% Page').reset_index()
    summary_cnt = merged_data.pivot_table(index=['PageId','WebpageLink','ExpectedLanguage'], columns='MasterPred',values='PredCnt').reset_index()

    column_list = ['Confidence1', 'Confidence2', 'Confidence3', 'MasterPredSumConfidences']
    for column in column_list:
        combined_data[column] = combined_data[column].apply(lambda x: int(x*100) if not math.isnan(x) else x)
        combined_data.rename(index=str, inplace=True, columns={column: '% '+column})

    # column_list = [i for i in summary_norm.columns if i not in ['PageId','WebpageLink','ExpectedLanguage']]
    # for column in column_list:
    #     summary_norm[column] = summary_norm[column].apply(lambda x: int(x*100) if not math.isnan(x) else x)
    #     summary_norm.rename(index=str, inplace=True, columns={column: '% '+column})

    column_list = ['% Page']
    for column in column_list:
        merged_data[column] = merged_data[column].apply(lambda x: int(x*100) if not math.isnan(x) else x)

    with pd.ExcelWriter('results/'+str(start.strftime('%Y%m%d%H%M'))+'_modelOutput.xlsx') as writer:
        merged_data.to_excel(writer, index=False, encoding='utf_8_sig', sheet_name='PageSummaries')
        combined_data.to_excel(writer, index=False, encoding='utf_8_sig', sheet_name='WordDetails')
        # summary_cnt.to_excel(writer, index=False, encoding='utf_8_sig', sheet_name='PivotSummaries')
        # summary_norm.to_excel(writer, index=False, encoding='utf_8_sig', sheet_name='PercentSummaries')

    return summary_norm, summary_cnt, combined_data, merged_data, normOutputDf