#!/usr/bin/python3
"""
Gather data from an API (Task 1)
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    user = requests.get('{}/users/{}'.format(base_url, user_id))
    task = requests.get('{}/todos?userId={}'.format(base_url, user_id))

    user_out = user.json()
    task_out = task.json()

    done_tasks = [x for x in task_out if x.get('completed') is True]

    filename = '{}.json'.format(user_id)
    out = {user_out.get('id'): []}

    with open(filename, "w") as file:
        for elem in task_out:
            data = {
                    'task': elem.get('title'),
                    'completed': elem.get('completed'),
                    'username': user_out.get('username')
            }
            out.get(user_out.get('id')).append(data)
        json.dump(out, file)
