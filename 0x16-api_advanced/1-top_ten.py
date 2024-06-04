#!/usr/bin/python3
"""Return top ten posts for a subreddit."""

import requests


def top_ten(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {"limit": 10}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)\
        AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 404:
        print("None")
        return
    total = response.json()["data"]["children"]
    for a in total:
        print(a['data']['title'])
