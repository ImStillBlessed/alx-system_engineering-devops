#!/usr/bin/python3
"""
This module retrieves fake data from REST API and exports it to JSON format.
"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        user_response = urllib.request.urlopen(url).read()
        todos_response = urllib.request.urlopen(todos_url).read()

        user_data = json.loads(user_response.decode('utf-8'))
        todos_data = json.loads(todos_response.decode('utf-8'))

        user_id = user_data.get('id')
        user_name = user_data.get('username')

        json_data = {user_id: []}

        for todo in todos_data:
            task_completed_status = todo.get('completed')
            task_title = todo.get('title')
            json_data[user_id].append({
                'task': task_title,
                'completed': task_completed_status,
                'username': user_name
            })

        json_file_name = f"{user_id}.json"
        with open(json_file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data has been exported to {json_file_name}")

    except Exception as e:
        print(f"Error: {e}")
