#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers)for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import json
import urllib.request


def number_of_subscribers(subreddit):
    """
    this function returns the number of subscribers for an account
    0 if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        req = urllib.request.Request(url, headers=headers)
        user_data = urllib.request.urlopen(req).read()
        json_data = json.loads(user_data.decode('utf-8'))
        subscribers = json_data['data']['subscribers']
        return subscribers
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return 0
        else:
            print("Error:", e)
            return 0
    except Exception as e:
        print("Error:", e)
        return 0
