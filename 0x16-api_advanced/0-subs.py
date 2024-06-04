#!/usr/bin/python3
"""Return No of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)\
        AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False,)
    if response.status_code == 404:
        return 0
    total = response.json().get("data").get("subscribers")
    return total
