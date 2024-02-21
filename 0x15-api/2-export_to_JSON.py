#!/usr/bin/python3
""" 1-export_to_JSON.py - export data in the JSON format."""

if __name__ == "__main__":
    import json
    import sys
    import requests

    user_id = sys.argv[1]
    td_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    usr_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        td_list = requests.get(td_url).json()
        user = requests.get(usr_url).json()

        if not td_list or not user:
            print("Employee not found")

        content = {
            user_id: [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user["username"]
                }
                for task in td_list
            ]
        }

        with open(f'{user_id}.json', mode='w') as file:
            json.dump(content, file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
