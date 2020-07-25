import json

from src.utils.apihandler import TwitterApiHandler, TWITTER_BEARER
from src.utils.twitter_auth.creds import BEARER_HEADER

twitter = TwitterApiHandler(headers=BEARER_HEADER)

params = {"q": "MAGA", "count": 10, "result_type": "mixed"}
tweets = twitter.get_tweet_search(params)

tweet_objects = []
for i in range(len(tweets["statuses"])):
    tweet_objects.append(tweets["statuses"][i])

user_objects = []
for i in range(len(tweets["statuses"])):
    user_objects.append(tweets["statuses"][i]["user"])

with open("users.json", "w") as outfile:
    json.dump(user_objects, outfile)

user_ids = []
for i in range(len(tweets["statuses"])):
    user_ids.append(tweets["statuses"][i]["user"]["id"])

for i in user_ids:
    params = {"user_id": i, "count": 5}
    timeline = twitter.get_user_timeline(params)
    for i in range(len(timeline)):
        tweet_objects.append(timeline[i])

with open("tweets.json", "w") as outfile:
    json.dump(tweet_objects, outfile)
