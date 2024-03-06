#!/usr/bin/python3
""" 3-dictionary_of_list_of_dictionaries.py - Python script to export data
in the JSON format -all users version-"""

if __name__ == "__main__":
    import json
    import requests

    td_url = "https://jsonplaceholder.typicode.com/todos"
    usr_url = "https://jsonplaceholder.typicode.com/users"

    try:
        td_list = requests.get(td_url).json()
        user_list = requests.get(usr_url).json()

        if not td_list or not user_list:
            print("No tasks or users found")
            exit(1)

        user_dict = {user["id"]: user for user in user_list}

        content = {
            str(user_id): [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_dict[task["userId"]]["username"]
                }
                for task in td_list
                if task["userId"] == user_id
            ]
            for user_id in user_dict.keys()
        }

        with open("todo_all_employees.json", mode='w') as file:
            json.dump(content, file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
