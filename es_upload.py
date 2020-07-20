from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

from src.utils.apihandler import TwitterApiHandler
from src.utils.twitter_auth.creds import BEARER_HEADER

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

twitter = TwitterApiHandler(headers=BEARER_HEADER)
params = {"q": "qanon", "count": 50}
payload = twitter.get_tweet_search(params)

count = 1
for i in payload['statuses']:

    document = i

    es.index(index="tweets", doc_type="_doc", id=count, body=document)

    print(es.get(index="tweets", doc_type="_doc", id=count))

    count += 1    