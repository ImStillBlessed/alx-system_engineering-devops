#!/usr/bin/python3
"""
This module retrieves fake data from REST API and saves it to
a csv file.
"""
import csv
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
    filename = f"{sys.argv[1]}.csv"

    with open(filename, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'status', 'title']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos_json:
            status = todo.get('completed')
            title = todo.get('title')
            writer.writerow({
                'id': sys.argv[1],
                'name': name,
                'status': str(status),
                'title': title
                })
