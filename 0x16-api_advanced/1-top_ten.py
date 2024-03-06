#!/usr/bin/python3
"""
1-top_ten.py - prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, params={"limit" : 10}, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = response.json().get("data")
    for i in data.get("children"):
        print(i.get("data").get("title"))
