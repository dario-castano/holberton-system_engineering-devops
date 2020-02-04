# !/usr/bin/python3
"""
Gather data from an API (Task 1)
"""
import csv
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

    filename = '{}.csv'.format(user_id)

    with open(filename, "w") as output:
        writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_ALL)
        for elem in task_out:
            data = [
                user_out.get('id'),
                user_out.get('username'),
                elem.get('completed'),
                elem.get('title')
            ]
            writer.writerow(data)
