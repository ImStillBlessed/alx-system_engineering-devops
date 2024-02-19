#!/usr/bin/python3
"""
This module retrieves fake data from REST API and displays it.
"""
import requests
import sys

def fetch_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()

        if user_response.status_code != 200 or todo_response.status_code != 200:
            print("Failed to retrieve data. Please check the employee ID and try again.")
            return

        employee_name = user_data['name']
        total_tasks = len(todo_data)
        completed_tasks = [task['title'] for task in todo_data if task['completed']]

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task_title in completed_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_progress(employee_id)
