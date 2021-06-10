#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import csv

csv.field_size_limit(100000000)

dic = []
with open('diagnosis7.csv', 'r', encoding='utf-8') as f:
    file_reader = csv.reader(f, delimiter = ",")
    for row in file_reader:
        dic.append(row)

# print(len(dic[0][1]))
for el in list(dic[0][1]):
    print(json.loads(el))

