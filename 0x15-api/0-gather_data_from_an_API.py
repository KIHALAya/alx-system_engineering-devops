#!/usr/bin/python3
""" 0-gather_data_from_an_API.py - returns information about TODO list progress
for a given employee ID."""

if __name__ == "__main__":
    import requests
    import sys

    employee_id = sys.argv[1]
    td_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    usr_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        td_list = requests.get(td_url).json()
        user = requests.get(usr_url).json()

        if not td_list or not user:
            print("Employee not found")

        completed_tasks = [tsk['title'] for tsk in td_list if tsk['completed']]
        total_tasks = len(td_list)

        print("Employee {} is done with tasks({}/{}):".format(
            user['name'], len(completed_tasks), total_tasks))
        for task_title in completed_tasks:
            print("\t {}".format(task_title))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
