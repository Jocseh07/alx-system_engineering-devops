#!/usr/bin/python3
"""Query reddit API and return list containing title of all hot articles."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return list of all hot articles for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {
        "after": after,
        "count": count,
        "limit": 100,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)\
        AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 404:
        return None

    total = response.json().get("data")
    after = total.get("after")
    count += total.get("dist")
    for a in total.get("children"):
        hot_list.append(a.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count=count)
    return hot_list
