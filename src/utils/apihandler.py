import requests
import json

from .urls import TWITTER_STANDARD_SEARCH_URL
from .urls import TWITTER_FRIENDSHIPS_LOOKUP_URL
from .urls import TWITTER_USER_LOOKUP_URL
from .urls import TWITTER_USER_SEARCH_URL
from .urls import TWITTER_FOLLOWERS_IDS_URL
from .urls import TWITTER_FRIENDS_IDS_URL
from .urls import TWITTER_TRENDS_PLACE_URL
from .twitter_auth.creds import BEARER_HEADER


class ApiHandler:
    def get_req(url: str, headers: dict, params: dict) -> dict:
        raise NotImplementedError("Abstract method not implemented")

    def post_req():
        raise NotImplementedError("Abstract method not implemented")


class TwitterApiHandler(ApiHandler):
    def __init__(self, headers):
        self.headers = headers

    def get_req(self, url: str, headers: dict, params: dict) -> dict:
        """Performs a GET request and returns the JSON response"""
        resp = requests.get(url, headers=self.headers, params=params)
        json_resp = json.loads(resp.content)
        return json_resp

    def post_req():
        pass

    def get_tweet_search(self, params: dict) -> dict:
        """Calls a standard (free) search on Tweets.
        Expects params (dict):
        q (str): Required
            Keyword to search on.
        result_type (str): Optional
            Either recent, popular, or mixed.
        count (int): Optional
            Number of Tweet Objects to return.
        geocode (str): Optional
            Geotagged, if enabled, or falls back to Twitter profile location.
            Formatted as 'latitude,longitude,radius'.
        since_id (int): Optional
            Results with an ID greater than (that is, more recent than)
            the specified ID

        Returns (dict):
        Tweet Objects and search metadata."""
        return self.get_req(url=TWITTER_STANDARD_SEARCH_URL,
                            headers=BEARER_HEADER,
                            params=params)

    def get_followers(self, params: dict) -> dict:
        """Get followers of a user.
        Expects params (dict):
        user_id (int): Optional
            User id to get followers of.
        screen_name (str): Optional
            @Handle to get followers of.
        cursor (int): Optional
            The response from the API will include a previous_cursor
            and next_cursor to allow paging back and forth. Default is
            -1 which means the first page.
        count (int): Optional
            Limit number of ids to return.

        Returns (dict):
        {ids, next_cursor, previous cursor}."""
        return self.get_req(url=TWITTER_FOLLOWERS_IDS_URL,
                            headers=BEARER_HEADER,
                            params=params)

    def get_friends(self, params: dict) -> dict:
        """Get friends (following) of a user.
        Expects params (dict):
        user_id (int): Optional
            User id to get friends of.
        screen_name (str): Optional
            @Handle to get friends of.
        cursor (int): Optional
            The response from the API will include a previous_cursor
            and next_cursor to allow paging back and forth. Default is
            -1 which means the first page.
        count (int): Optional
            Limit number of ids to return.

        Returns (dict):
        {ids, next_cursor, previous cursor}."""
        return self.get_req(url=TWITTER_FRIENDS_IDS_URL,
                            headers=BEARER_HEADER,
                            params=params)

    def get_friendships(self, params: dict) -> dict:
        """Get friendships of a user as connections which can be:
        following, following_requested, followed_by, none, blocking,
        muting. Uses OAuth 1 instead of OAuth 2.
        Expects params (dict):
        user_id (int): Optional
            User id to get friends of.
        screen_name (str): Optional
            @Handle to get friends of.

        Returns (dict):
        Ids and their relationship to given User."""
        return self.get_req(url=TWITTER_FRIENDSHIPS_LOOKUP_URL,
                            headers=BEARER_HEADER,
                            params=params)

    def get_user_objects(self, params: dict) -> dict:
        """Fully hydrates User Objects from ids.
        Expects params (dict):
        user_id (list): Optional
            User ids to get User Objects of.
        screen_name (list): Optional
            @Handles to get User Objects of.

        Returns (dict):
        User Objects."""
        return self.get_req(url=TWITTER_USER_LOOKUP_URL,
                            headers=BEARER_HEADER,
                            params=params)

    def get_user_search(self, params: dict) -> dict:
        """Calls a search on Users. Uses OAuth 1 instead of OAuth 2.
        Expects params (dict):
        q (str): Required
            Keyword to search on, like topical interest, full name,
            company name, location, or other criteria.
        page (int): Optional
            Specifies the page of results to retrieve.
        count (int): Optional
            The number of potential user results to retrieve per page,
            max 20.

        Returns (dict):
        User Objects."""
        return self.get_req(url=TWITTER_USER_SEARCH_URL,
                            headers=BEARER_HEADER,
                            params=params)

    def get_trends_search(self, params: dict) -> dict:
        """Calls a search on trends by WOEID and returns top 50.
        Expects params (int):
        id (int): Required
            Yahoo! Where On Earth ID

        Returns (dict):
        {name, url, promoted_content, tweet_volume}."""
        return self.get_req(url=TWITTER_TRENDS_PLACE_URL,
                            headers=BEARER_HEADER,
                            params=params)


if __name__ == "__main__":
    pass

