import os
import sys
import json
import time

import pandas as pd

from src.utils.apihandler import TwitterApiHandler
from src.utils.twitter_auth.creds import BEARER_HEADER
from src.utils.transform.flattener import flatten_json
from src.utils.transform.json_to_csv import turn_json_to_pd_csv
from src.utils.transform.list_to_csv import turn_list_to_pd_csv
from src.utils.boto import upload_to_s3
from src.utils.constants import QANON_URL
from src.utils.scraper import scrape_for_wiki_anchors
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

twitter = TwitterApiHandler(headers=BEARER_HEADER)
params = {"q": "qanon", "count": 10}
payload = twitter.get_tweet_search(params)

flattened_twitter = pd.json_normalize(data=payload["statuses"])
df = flattened_twitter[
    [
        "created_at",
        "id",
        "text",
        "retweet_count",
        "user.description",
        "user.followers_count",
    ]
]


def score_sentiment(text):
    return analyzer.polarity_scores(text)["compound"]


def apply_sentiment(df):
    df["compound"] = df["text"].apply(score_sentiment)
    return df
