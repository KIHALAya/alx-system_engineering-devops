#!/usr/bin/python3
"""
0-subs.py - returns the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers of a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = response.json().get("data")
    return (data.get("subscribers"))
