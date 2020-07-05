from pprint import pprint
import os
import sys

from utils.apihandlerapihandler import TwitterApiHandler
from utils.twitter_auth.creds import BEARER_HEADER

# why wont get freidnshisp work and how do i chain methods?
# Need certaain apis to inherit bearer header

twitter = TwitterApiHandler(headers=BEARER_HEADER)
params = {"q": "soccer"}
pprint(twitter.get_tweet_search(params))

# twitter = TwitterApiHandler(headers=BEARER_HEADER)
# params = {"user_id": [171598736, 1244907337996959744]}
# pprint(twitter.get_user_objects(params))

# params = {"user_id": [171598736, 1244907337996959744]}
# twitter = TwitterApiHandler(headers=BEARER_HEADER, params=params)
# pprint(twitter.get_user_objects(params))

# params = {"q": "soccer", "count": 5}
# twitter = TwitterApiHandler(headers=BEARER_HEADER, params=params)
# pprint(twitter.get_user_search(params))
# 2379574

# params = {"id": 2379574}
# twitter = TwitterApiHandler(headers=BEARER_HEADER, params=params)
# pprint(twitter.get_trends_search(params))

