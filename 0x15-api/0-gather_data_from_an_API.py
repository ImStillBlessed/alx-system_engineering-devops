#!/usr/bin/python3
"""
This module retrieves fake data from REST API and displays it.
"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{user_id}'
    todo_url = f'{base_url}/todos?userId={user_id}'

    user = urllib.request.urlopen(user_url).read()
    todos = urllib.request.urlopen(todo_url).read()

    user_json = json.loads(user.decode('utf-8'))
    todos_json = json.loads(todos.decode('utf-8'))
    name = user_json.get('name')
    complete = [x for x in todos_json if x.get('completed')]

    print(f'Employee {name} is done\
 with tasks({len(complete)}/{len(todos_json)}):')
    for task in complete:
        print(f'\t {task.get("title")}')
