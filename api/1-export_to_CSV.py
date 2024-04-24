import csv
import json
import requests
import sys

#!/usr/bin/python3
"""Gather data from an API"""


if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = sys.argv[1]
        res = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

        response_usr_todo = json.loads(res.text)
        user = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        user_response = json.loads(user.text)
        user_name = user_response["username"]
        with open(f"{user_id}.csv", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in response_usr_todo:
                csv_list = [str(todo['userId']), str(user_name), str(todo['completed']), str(todo['title'])]
                writer.writerow(csv_list)
