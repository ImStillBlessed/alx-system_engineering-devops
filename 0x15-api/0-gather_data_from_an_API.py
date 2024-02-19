#!/usr/bin/python3
"""
This module retrieves fake data and displays it USING
REST API
"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + id

    user = urllib.request.urlopen(url).read()
    todos = urllib.request.urlopen(url + '/todos').read()

    user_json = json.loads(user.decode('utf-8'))
    todos_json = json.loads(todos.decode('utf-8'))
    name = user_json.get('name')
    complete = [x for x in todos_json if x.get('completed') == True]

    print(f'Employee {name} is done with tasks({len(complete)}/{len(todos_json)}):')
    for task in complete:
        print(f'\t {task.get('title')}')
