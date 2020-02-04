#!/usr/bin/python3
"""
Gather data from an API (Task 1)
"""
import json
import requests

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'

    users_out = requests.get('{}/users'.format(base_url)).json()
    tasks_out = requests.get('{}/todos'.format(base_url)).json()

    filename = 'todo_all_employees.json'
    out = dict()

    for user in users_out:
        out.update({user.get('id'): []})
        for elem in tasks_out:
            if elem.get('userId') == user.get('id'):
                data = {
                        'task': elem.get('title'),
                        'completed': elem.get('completed'),
                        'username': user.get('username')
                }
                out.get(user.get('id')).append(data)

    with open(filename, "w") as file:
        json.dump(out, file)
