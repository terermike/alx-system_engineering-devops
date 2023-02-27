#!/usr/bin/python3
"""This module has a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints 3 the titles of
    the first 10 hot posts listed for a given subreddit"""

    headers = {'User-Agent': 'Google Chrome Version 110.0.5481.105'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print('None')
