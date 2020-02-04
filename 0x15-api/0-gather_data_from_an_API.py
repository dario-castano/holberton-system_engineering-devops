#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    user = requests.get('{}/users/{}'.format(base_url, user_id))
    task = requests.get('{}/todos?userId={}'.format(base_url, user_id))

    user_out = user.json()
    task_out = task.json()

    all_tasks = len(task_out)
    done_tasks = len([x for x in task_out if x.get('completed') is True])

    print('Employee {} is done with tasks({}/{}):'
          .format(user_out.get('name'), done_tasks, all_tasks))

    for task in task_out:
        if task.get('completed') is True:
            print('\t {}'.format(task.get('title')))
