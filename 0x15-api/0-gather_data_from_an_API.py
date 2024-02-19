#!/usr/bin/python3
"""
This module retrieves fake data from REST API and displays it.
"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    user = urllib.request.urlopen(url).read()
    todos = urllib.request.urlopen(url + '/todos').read()

    user_json = json.loads(user.decode('utf-8'))
    todos_json = json.loads(todos.decode('utf-8'))
    name = user_json.get('name')
    complete = [x for x in todos_json if x.get('completed')]

    print(f'Employee {name} is done\
 with tasks({len(complete)}/{len(todos_json)}):')
    for task in complete:
        print(f'\t {task.get("title")}')
