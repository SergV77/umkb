#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv
import time

url = 'https://cs.socmedica.com/api/umkb/getsemanticnewbigid'
#url = 'https://cs.socmedica.com/api/umkb/getsemantic'


print('Начало запросов в UMKB')
tic = time.perf_counter()
allSymptoms = []
symptoms = []
param = {'key':'6a1eb6fa9dd973ac',
         'lib':[25],
         'level': 1502,
         'deep': 1,
         'text': 'аппендицит'
         }

response = requests.post(url, param)
outs = response.json()
print(outs)
if outs['names'] != None:
    for out in outs['names'].values():
        print(out)
        symptoms.append(out)
print(symptoms)
if len(symptoms) != 0:
    allSymptoms.append(symptoms)

print('Конец запросов в UMKB')
print('*'*100)
print(len(allSymptoms[0]))
print(allSymptoms)
toc = time.perf_counter()
print('Конец работы')
print(f"Вычисление заняло {toc - tic:0.4f} секунд")