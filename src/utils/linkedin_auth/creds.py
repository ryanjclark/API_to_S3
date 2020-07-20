import os
import requests
import base64

# TODO: Import URL

AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
CLIENT_KEY = "7769y3afrhc94j"
CLIENT_SECRET = "yJ0ze3u6uJXV6x69"

key_secret = "{}:{}".format(CLIENT_KEY, CLIENT_SECRET).encode("ascii")
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode("ascii")

auth_headers = {
    # "client_id": "{}".format(CLIENT_KEY),
    # "client_secret": "{}".format(CLIENT_SECRET),
    "Host": "www.linkedin.com",
    "Content-Type": "application/x-www-form-urlencoded",
}
auth_data = {"grant_type": "client_credentials", "client_id": CLIENT_KEY, "client_secret": CLIENT_SECRET}
auth_data = "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=7769y3afrhc94j&redirect_uri=https%3A%2F%2Fdev.example.com%2Fauth%2Flinkedin%2Fcallback&state=fooobar&scope=r_liteprofile%20r_emailaddress%20w_member_social"
auth_resp = requests.get(AUTH_URL, headers=auth_headers, params=auth_data)
# access_token = auth_resp.json()["access_token"]
# BEARER_HEADER = {"Authorization": "Bearer {}".format(access_token)}
print(auth_resp)