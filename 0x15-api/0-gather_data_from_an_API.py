#!/usr/bin/python3
"""
This module retrieves fake data and displays it USING
REST API
"""
import sys
import urllib.request

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    with urllib.request.urlopen(url) as response:
        json_data = response.json()
        print(json_data)
