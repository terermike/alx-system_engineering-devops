#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    eployee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + eployee_id

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response  = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

     print("Employee {} is done with tasks({}/{}):"
           .format(employee_name, done, len(tasks)))

    for task in done_tasks:
         print("\t {}".format(task.get('title')))
