#!/usr/bin/python3
""" 1-export_to_CSV.py - export data in the CSV format."""

if __name__ == "__main__":
    import csv
    import sys
    import requests

    employee_id = sys.argv[1]
    td_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    usr_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        td_list = requests.get(td_url).json()
        user = requests.get(usr_url).json()

        if not td_list or not user:
            print("Employee not found")
            sys.exit(1)

        with open(f'{employee_id}.csv', mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            for item in td_list:
                writer.writerow([
                     item["userId"],
                     user["username"],
                     "True" if item["completed"] else "False",
                     item["title"]
                     ])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
