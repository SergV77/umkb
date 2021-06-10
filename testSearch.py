#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

url = "https://cs.socmedica.com/api/anj/SearchConceptList"

words = []
with open('diagnosis.csv', 'r', encoding='utf-8') as f:
    load_file = csv.reader(f)
    for row in load_file:
        #print(row)
        words.append(row)

diagnosis = words[0]

param = {
    "key": "ac6c0cd189020a8b",
    "texts": diagnosis,
    "libs": [25],
    "chain": 1,
    "deep":1,
    "linguistics": 0,
    "secondary": 0,
    "greedy": 0
    }

nat_json = json.dumps(param)
headers = {'Content-type': 'application/json'}

response = requests.post(url, nat_json, headers=headers)
outs = response.json()

nosology = {}
for out in outs['concepts']:
    if out[0]['idlevel'] == 184:
        nosology[out[0]['id']] = out[0]['name']

fieldnames = ['id', 'name']
with open('diagnosis4.csv', mode='w', encoding='utf-8', newline='') as file:
    file_writer = csv.DictWriter(file, fieldnames=fieldnames)
    file_writer.writeheader()
    for k, v in nosology.items():
        file_writer.writerow({'id': k, 'name': v})
