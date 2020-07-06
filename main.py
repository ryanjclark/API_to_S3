import os
import sys
import json
import time

import pandas as pd

from src.utils.apihandler import TwitterApiHandler
from src.utils.twitter_auth.creds import BEARER_HEADER
from src.utils.transform.flattener import flatten_json
from src.utils.transform.json_to_csv import turn_json_to_pd_csv
from src.utils.boto import upload_to_s3
from src.utils.constants import QANON_URL
from src.utils.scraper import scrape_for_wiki_anchors

timestr = time.strftime("%Y%m%d-%H%M%S")
twitter_output_filename = "twitter_data_{}.csv".format(timestr)
wiki_output_filename = "wiki_data_{}.csv".format(timestr)
BUCKET_NAME = os.environ.get('BUCKET_NAME')

twitter = TwitterApiHandler(headers=BEARER_HEADER)
params = {"q": "qanon", "count": 50}
payload = twitter.get_tweet_search(params)

flattened = flatten_json(payload)
turn_json_to_pd_csv(flattened, twitter_output_filename)

scrape_for_wiki_anchors(url=QANON_URL, output=wiki_output_filename)

upload_to_s3(output=twitter_output_filename, bucket=BUCKET_NAME)
upload_to_s3(output=wiki_output_filename, bucket=BUCKET_NAME)

