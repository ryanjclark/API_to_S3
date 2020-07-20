import json

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

host = 'search-twitter-es-c4ddme6tvpke7xdll2fzobefyy.us-east-2.es.amazonaws.com'
region = 'us-east-2'

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

def search(es_object, index_name, search):
    res = es_object.search(index=index_name, body=search)
    return res

tweet_contains_maga_query = {
                                'query': 
                                    {
                                        'match': 
                                            {'text': 'maga'}
                                    }
                            }
tweet_contains_maga_result = search(es, 'tweets', tweet_contains_maga_query)
print("Tweets containing MAGA: {}".format(len(tweet_contains_maga_result)))

tweet_contains_trump_or_maga_query = {
                                        "query": {
                                            "match" : {
                                                "text" : "(maga) OR (trump) OR (2020)"
                                            }
                                        }
                                    }
tweet_contains_maga_result = search(es, 'tweets', tweet_contains_trump_or_maga_query)
print("Tweets containing MAGA, Trump OR 2020: {}".format(len(tweet_contains_maga_result)))

tweet_is_retweet_or_quote = {
                                "bool" : {
                                    "should" : [
                                        { "term" : { "is_quote_status" : "true" } },
                                        { "term" : { "retweeted" : "true" } }
                                    ],
                                    "minimum_should_match" : 1
                                }
                            }
print("Tweets that are either retweets or quoted tweets: {}".format(len(tweet_is_retweet_or_quote)))

tweet_with_more_than_10_likes = {
                                    "query": {
                                        "range" : {
                                            "favorite_count" : {
                                                "gte" : 10
                                            }
                                        }
                                    }
                                }
print("Tweets with more than 10 likes: {}".format(len(tweet_with_more_than_10_likes)))