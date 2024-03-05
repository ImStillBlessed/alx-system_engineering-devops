#!/usr/bin/python3
"""
This method queries the Reddit API 
"""
import json
import urllib.request


def top_ten(subreddit):
    """
    Function queries the Reddit API and 
    prints the titles of the first 10 hot posts listed for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        req = urllib.request.Request(url, headers=headers)
        user_data = urllib.request.urlopen(req).read()
        json_data = json.loads(user_data.decode('utf-8'))
        posts = json_data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(None)
    except Exception as e:
        print(None)

top_ten("programming")