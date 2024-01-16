#!/usr/bin/python3
"""Script that prints out top ten hottest posts"""

import requests


def top_ten(subreddit):
    """the funct that fetches top 10 posts"""
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    limits = 10

    response = requests.get(
        apiUrl, headers={"user-agent": userAgent}, params={"limit": limits})
    if not response:
        print('None')
        return
    response = response.json()
    list_obj = response['data']['children']
    for obj in list_obj:
        print(obj['data']['title'])
    return
