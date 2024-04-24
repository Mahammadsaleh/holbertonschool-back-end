#!/usr/bin/python3
import requests
import csv
import json
import sys


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
if len(sys.argv) == 2:
    res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                       f'{sys.argv[1]}/todos')
    response = json.loads(res.text)
    print(res.text)
    with open(f"{sys.argv[1]}.csv","w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(response)
    # response = csv.loads(res.text)
    # all_task = len(response)