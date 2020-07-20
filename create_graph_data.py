import json

from src.utils.apihandler import TwitterApiHandler, TWITTER_BEARER
from src.utils.twitter_auth.creds import BEARER_HEADER

twitter = TwitterApiHandler(headers=BEARER_HEADER)

params = {"q": "qanon", "count": 5, "result_type": "mixed"}
tweets = twitter.get_tweet_search(params)

all_user_objects = []
for i in range(len(tweets['statuses'])):
    all_user_objects.append(tweets['statuses'][i]['user'])


user_ids = []
for i in range(len(tweets['statuses'])):
    user_ids.append(tweets['statuses'][i]['user']['id'])

follower_user_ids = []
for i in user_ids:
    params = {"user_id": i, "count": 5}
    followers = twitter.get_followers(params)
    for i in followers['ids']:
        follower_user_ids.append(i)

params = {"user_id": follower_user_ids}
follower_user_obj = twitter.get_user_objects(params)

all_user_objects = all_user_objects + follower_user_obj

with open('data.json', 'w') as outfile:
    json.dump(all_user_objects, outfile)