#!/usr/bin/python3
"""Return No of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json()["data"]["subscribers"]
