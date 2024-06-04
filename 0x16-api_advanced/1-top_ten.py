#!/usr/bin/python3
"""Return top ten posts for a subreddit."""

import requests


def top_ten(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {"limit": 10}
    response = requests.get(url, allow_redirects=False, params=params)
    if response.status_code != 200:
        print("None")
        return
    total = response.json()["data"]["children"]
    for a in total:
        print(a['data']['title'])
