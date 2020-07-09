import os
import requests
import base64

# TODO: Import URL

BASE_TWITTER_URL = "https://api.twitter.com/"
AUTH_URL = "{}oauth2/token".format(BASE_TWITTER_URL)
CLIENT_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CLIENT_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")

key_secret = "{}:{}".format(CLIENT_KEY, CLIENT_SECRET).encode("ascii")
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode("ascii")

auth_headers = {
    "Authorization": "Basic {}".format(b64_encoded_key),
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
}
auth_data = {"grant_type": "client_credentials"}

auth_resp = requests.post(AUTH_URL, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()["access_token"]
BEARER_HEADER = {"Authorization": "Bearer {}".format(access_token)}
