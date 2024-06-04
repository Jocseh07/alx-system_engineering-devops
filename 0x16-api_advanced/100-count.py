#!/usr/bin/python3
"""Query reddit API and return list containing title of all hot articles."""

import requests


def count_words(subreddit, word_list, found={}, after="", count=0):
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
        titles = (a.get("data").get("title")).lower().split()
        for word in word_list:
            if word.lower() in titles:
                num = 0
                for title in titles:
                    if title.lower() == word.lower():
                        num += 1
                if found.get(word) is None:
                    found[word] = num
                else:
                    found[word] += num

    if after is None:

        found = sorted(found.items(), key=lambda x: x[1], reverse=True)

        for k, v in found:
            print(f"{k}: {v}")
    else:
        count_words(subreddit, word_list, found, after, count)
