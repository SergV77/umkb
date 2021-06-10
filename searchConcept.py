#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

url = "https://cs.socmedica.com/api/anj/SearchConceptList"

words = []
with open('diagnosis2.csv', 'r', encoding='utf-8') as f:
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

nosology = []
for out in outs['concepts']:
    if len(out) != 0:
        if out[0]['lib'] == 25 and out[0]['idlevel'] in [1102, 183, 184, 920]:
            nosology.append(out[0]['name'])

with open('diagnosis.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=',')
    file_writer.writerow(nosology)
