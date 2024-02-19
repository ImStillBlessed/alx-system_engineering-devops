#!/usr/bin/python3
"""
This module retrieves fake data and displays it USING
REST API
"""

import sys
import requests


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    response = requests.get(url, id=user_id)
    json_data = response.json()
    print(json_data)
