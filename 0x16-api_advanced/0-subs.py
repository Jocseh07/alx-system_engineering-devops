#!/usr/bin/python3
"""Return No of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64;\
            rv:109.0) Gecko/20100101 Firefox/115.0"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False,)
    if response.status_code == 404:
        return 0
    total = response.json().get("data").get("subscribers")
    return total
