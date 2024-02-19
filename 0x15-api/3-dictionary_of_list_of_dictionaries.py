#!/usr/bin/python3
"""
This module retrieves fake data from REST API and exports it to JSON format for all employees.
"""
import json
import urllib.request

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    all_users_url = f'{base_url}/users'

    try:
        all_users_response = urllib.request.urlopen(all_users_url).read()
        all_users_data = json.loads(all_users_response.decode('utf-8'))

        all_employee_data = {}

        for user in all_users_data:
            user_id = user.get('id')
            username = user.get('username')

            todos_url = f'{base_url}/todos?userId={user_id}'
            todos_response = urllib.request.urlopen(todos_url).read()
            todos_data = json.loads(todos_response.decode('utf-8'))

            user_tasks = []
            for todo in todos_data:
                task_title = todo.get('title')
                completed = todo.get('completed')
                user_tasks.append({
                    'username': username,
                    'task': task_title,
                    'completed': completed
                })

            all_employee_data[user_id] = user_tasks

        json_file_name = 'todo_all_employees.json'
        with open(json_file_name, 'w') as json_file:
            json.dump(all_employee_data, json_file, indent=4)

    except Exception as e:
        print(f"Error: {e}")
