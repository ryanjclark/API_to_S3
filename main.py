import os
import sys
import json

import pandas as pd

from src.utils.apihandler import TwitterApiHandler
from src.utils.twitter_auth.creds import BEARER_HEADER
from src.utils.transform import flatten_json

twitter = TwitterApiHandler(headers=BEARER_HEADER)
# TODO: 50 records
params = {"q": "qanon"}

payload = twitter.get_tweet_search(params)

flattened = flatten_json(payload)

df = pd.Series(flattened).to_frame()
df.rename(columns={"0": "value"}, inplace=True)
df.to_csv('output.csv')

