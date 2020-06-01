import argparse
from model import run_model
import scraper

parser = argparse.ArgumentParser()
parser.add_argument('--lang', nargs='*', type=str, default=["en", "es", "de", "zh-CN"])
parser.add_argument('environment', help='The environment the tests will run on')
args = parser.parse_args()

scraper.sample(args.environment, args.lang)
run_model('2019 hackathon example.csv', '.')
