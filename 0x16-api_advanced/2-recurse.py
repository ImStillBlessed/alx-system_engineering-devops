#!/usr/bin/python3
"""
queries the Reddit API 
"""
import json
import urllib


import json
import urllib.request
import urllib.error

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        req = urllib.request.Request(url, headers=headers)
        user_data = urllib.request.urlopen(req, timeout=10).read()
        json_data = json.loads(user_data.decode('utf-8'))

        posts = json_data['data']['children']
        if not posts:
            if not hot_list:
                return None
            else:
                return hot_list

        for post in posts:
            hot_list.append(post['data']['title'])

        after = json_data['data']['after']
        return recurse(subreddit, hot_list, after)
    
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        else:
            print("Error:", e)
            return None
    except urllib.error.URLError as e:
        print("Error connecting to Reddit:", e)
        return None
    except Exception as e:
        print("Error:", e)
        return None
