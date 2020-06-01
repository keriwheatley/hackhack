from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import traceback
import time
import base64
import os
import sys
import platform
import multiprocessing
import shutil

"""
Place an Amazon - SNS notification order
"""


def order_pool_executor(execution_environment, code_list, threads=True):
    """
    This methods buils a multiprocessing pool to place multiple Simple Notification Service (Amazon) orders in parallel
    :param execution_environment:
    :param code_list:
    :param threads:
    :return:
    """
    pool = None
    results = []
    try:
        if threads:
            count = multiprocessing.cpu_count()
            pool = multiprocessing.Pool(count)
            execution_list = [(execution_environment, x) for x in code_list]
            results = pool.map(place_aws_order, execution_list)
        else:
            for item in language_code_list:
                output = place_aws_order((execution_environment, item), browser=False)
                results.append(output)
    except Exception as e:
        pass
        print(e)
    finally:
        if pool is not None:
            pool.close()
    return results


def place_aws_order(execution_config, browser=False):
    driver = None
    environment, lang_code = execution_config
    url = "https://{}.gravitant.net".format(environment)
    chrome_driver_parent_path = os.path.abspath(os.path.join(sys.argv[0], os.pardir))
    chrome_driver_path = chrome_driver_parent_path + "/chrome_driver/mac-chromedriver" \
        if str(platform.system()) in 'Darwin' else chrome_driver_parent_path + \
                                                   "/chrome_driver/linux-chromedriver"
    time.sleep(2)
    if not browser:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--lang={}'.format(lang_code))
        chrome_options.add_argument(
            '--no-sandbox')
        chrome_options.add_argument(
            '--disable-gpu')
        chrome_options.add_argument(
            '--window-size=1500,2000')
        chrome_options.add_argument(
            'disable-extensions')
        chrome_options.add_argument(
            '--test-type')
        driver = webdriver.Chrome(
            executable_path=chrome_driver_path,
            chrome_options=chrome_options,
            service_args=['--verbose'])
        driver.delete_all_cookies()
    else:
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False
        binary = FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox-bin')
        driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)
        driver.delete_all_cookies()
    if os.path.exists(chrome_driver_parent_path + "/screenshots/{}".format(lang_code)):
        shutil.rmtree(chrome_driver_parent_path + "/screenshots/{}".format(lang_code))
    os.makedirs(chrome_driver_parent_path + "/screenshots/{}".format(lang_code))
    api_object = ApiKeyScript(url, chrome_driver_path, driver, browser, lang_code)
    print("Ready to navigate:{}".format(id(api_object)))
    return api_object.navigate_aws()


class ApiKeyScript:
    def __init__(self, url, chrome_driver_path, driver, browser, lang_code):
        self.url = url
        self.chrome_driver_path = chrome_driver_path
        self.driver = driver
        self.browser = browser
        self.lang_code = lang_code

    def navigate_aws(self):
        """
        This method automatically grabs api key for given user in the system
        :param user_mapping:
        :param browser: True - Run with firefox binary, False - run in headless fashion on Jenkins server
        :return: boolean indicating if all api keys for all configured users was fetched successfully
        """
        order_id = None
        url_list = []
        username = "e2esvtapi+admin@gmail.com"
        password = base64.b64decode("R3Jhdml0YW50MTIzIQ ==").decode('utf-8')
        try:
            self.open_browser()
            print("Opened browser:".format(id(self)))
            self.driver.get_screenshot_as_file('screenshots/{}/browser.png'.format(self.lang_code))
            self._click_control('username')
            self._enter_text('username', username)
            self.driver.get_screenshot_as_file('screenshots/{}/username.png'.format(self.lang_code))
            self._click_control('continue-button')
            print("Hit continue:".format(id(self)))
            time.sleep(2)
            self._click_control('password')
            self._enter_text('password', password)
            self.driver.get_screenshot_as_file('screenshots/{}/password.png'.format(self.lang_code))
            self._click_control('signinbutton')
            time.sleep(2)
            print("Sign in successful")
            url_list.append(("Sign-In Page", self.driver.page_source))
            self.driver.get_screenshot_as_file('screenshots/{}/signed-in.png'.format(self.lang_code))
            current_window = self.driver.window_handles
            self._click_control("//a[@id = 'privacy-policy-link']", By.XPATH)
            new_window = self.driver.window_handles
            new_window = list(set(new_window) - set(current_window))[0]
            self.driver.switch_to.window(new_window)
            print("switch done")
            time.sleep(1)
            #self.driver.close()
            self.driver.switch_to.window(current_window[0])
            if self._control_exists('checkbox-verifyCheckboxId'):
                self._click_control('checkbox-verifyCheckboxId')
            self._click_control('bx--checkbox-label', By.CLASS_NAME)
            self._click_control('privacy-policy-modal_carbon-button_submit')
            time.sleep(1)
            print("checkbox modal verified")
            self.driver.get_screenshot_as_file('screenshots/{}/buy_service.png'.format(self.lang_code))
            self._click_control('catalogLinkId')
            time.sleep(2)
            self.driver.get_screenshot_as_file('screenshots/{}/catalog.png'.format(self.lang_code))
            self._click_control('button-storefront_carbon-button_configure')
            self.driver.get_screenshot_as_file('screenshots/{}/configure.png'.format(self.lang_code))
            print("Entered Main parameters page")
            time.sleep(3)
            url_list.append(("Main Parameters page", self.driver.page_source))
            self._click_control("//*[@id='text-input-main_params-serviceName']", By.XPATH)
            self._enter_text("//*[@id='text-input-main_params-serviceName']", "testinstance", By.XPATH)
            self.driver.get_screenshot_as_file('screenshots/{}/instance.png'.format(self.lang_code))
            self._click_control("//*[@id='bx--dropdown-single-parent_team']/li[1]", By.XPATH)
            time.sleep(2)
            self._click_control("dropdown-option_team_e2esvtapi_admin")
            self.driver.get_screenshot_as_file('screenshots/{}/team.png'.format(self.lang_code))
            time.sleep(3)
            self._click_control("e2esvtapi_env")
            self._click_control("//*[@id='e2esvtapi_env']/div[1]/div[2]/carbon-search/div/div/ul/li[1]", By.XPATH)
            time.sleep(1)
            self.driver.get_screenshot_as_file('screenshots/{}/env.png'.format(self.lang_code))

            self._click_control("e2esvtapi_app")
            time.sleep(1)
            self._click_control("//*[@id='e2esvtapi_app']/div/div[2]/carbon-search/div/div/ul/li[1]", By.XPATH)
            time.sleep(1)
            self.driver.get_screenshot_as_file('screenshots/{}/app.png'.format(self.lang_code))
            self._click_control("//*[@id='bx--dropdown-single-parent_provider-account']/li[1]", By.XPATH)
            time.sleep(1)
            self._click_control("dropdown-option_provider-account_e2esvtapi_admin_amazone2esvtapi_admin_amazon")
            time.sleep(1)
            self.driver.get_screenshot_as_file('screenshots/{}/provider.png'.format(self.lang_code))
            self._click_control("button-next-button-mainParams")
            time.sleep(1)
            self.driver.get_screenshot_as_file('screenshots/{}/nextpage.png'.format(self.lang_code))
            print("Entering Configuring region")
            self._click_control("//*[@id='bx--dropdown-single-parent_AWS::Region']/li[1]", By.XPATH)
            self._click_control("dropdown-option_AWS::Region_apnortheast1")
            self._click_control("button-next-button-additionalParams")
            time.sleep(2)
            self.driver.get_screenshot_as_file('screenshots/{}/topic.png'.format(self.lang_code))
            print("Entered topic page")
            self._click_control("text-input-topicName")
            self._enter_text("text-input-topicName", "testtopic")
            self._click_control("button-next-button-additionalParams")
            time.sleep(1)
            self.driver.get_screenshot_as_file('screenshots/{}/subscription.png'.format(self.lang_code))
            print("Entered Subscription page")
            self._click_control("text-input-endpoint")
            self._enter_text("text-input-endpoint", "http")
            self._click_control("button-next-button-additionalParams")
            time.sleep(1)
            self.driver.get_screenshot_as_file('screenshots/{}/revieworder.png'.format(self.lang_code))
            print("Entered review order")
            url_list.append(("Review Order Page", self.driver.page_source))
            self._click_control("button-quickPurchaseSubmit-button-reviewOrder")
            time.sleep(5)
            self.driver.get_screenshot_as_file('screenshots/{}/ordersubmitted.png'.format(self.lang_code))
            element = self.driver.find_element_by_id("order-number")
            order_id = element.text
            print("SUBMITTED ORDER: {}".format(order_id))
            url_list.append(("Order Submission Page", self.driver.page_source))
            self._click_control("button-order-submitted-modal_carbon-button")
            time.sleep(2)
            self._click_control('budgetLinkId')
            time.sleep(2)
            self._click_control('button-addBudgetaryUnitBtn')
            time.sleep(2)
            print("Entered budget page")
            url_list.append(("Budgetary Unit Page", self.driver.page_source))
            self.driver.get_screenshot_as_file('screenshots/{}/budget_unit.png'.format(self.lang_code))
            self._click_control('button-cancelAddBudgetaryUnit')
            time.sleep(2)
            self._click_control('conversionLinkId')
            time.sleep(2)
            self._click_control('button-addConversionRate')
            time.sleep(2)
            print("Entered currency conversion page")
            url_list.append(("Add Conversion Rate page", self.driver.page_source))
            self.driver.get_screenshot_as_file('screenshots/{}/currency_conversion.png'.format(self.lang_code))

        except Exception as e:
            print(e)
            print("Caught some exception")
            traceback.print_exc(e)
            self.driver.get_screenshot_as_file('screenshots/{}/exception.png'.format(self.lang_code))
        finally:
                if self.driver is not None:
                    self.driver.quit()
                return self.lang_code, order_id, url_list

    def open_browser(self):
        self.driver.get(self.url)
        time.sleep(2)

    def _control_exists(self, element_id):
        exists = True
        try:
            self.driver.find_element_by_id(element_id)
        except NoSuchElementException:
            exists = False
        return exists

    def _enter_text(self, element_value, text, by=By.ID):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((by, element_value))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.send_keys(text)
        actions.perform()

    def _click_control(self, element_value, by=By.ID):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((by, element_value))
        )
        element.click()


if __name__ == "__main__":
    #Pool executor
    #language_code_list = ["en", "es", "fr", "de", "it", "nl", "zh-CN"]
    language_code_list = ["en", "es", "de", "zh-CN"]
    environment = "cb-api-auto-test-release"
    test_results = order_pool_executor(environment, language_code_list, threads=True)
    for item in test_results:
        print(item[0], item[1], item[2][0], len(item[2]))



