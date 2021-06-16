#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

url = 'https://cs.socmedica.com/api/umkb/getsemanticnewbigid'
#url = 'https://cs.socmedica.com/api/umkb/getsemantic'

diagnosis = ['Аппендицит', 'Инфаркт миокарда', 'острая респираторная вирусная инфекция', 'грипп', 'пневмония', 'острый тонзиллит', 'Холецистит', 'Язва желудка']
allSymptoms = []
for word in diagnosis:
    symptoms = []
    param = {'key':'6a1eb6fa9dd973ac',
             'lib':[25],
             'level': 1502,
             'deep': 0,
             #'text': word
             }

    response = requests.post(url, param)
    outs = response.json()
    print(outs)

    for out in outs['names'].values():
        print(out)
        #print(out['chance'])
        symptoms.append(out)
        #symptomsId.append(out['id'])

    allSymptoms.append(symptoms)


print(len(allSymptoms))
print(allSymptoms)

# with open('diagnosis.csv', mode='w', encoding='utf-8') as file:
#     file_writer = csv.writer(file)
#     #for i in range(len(allSymptoms)):
#     for symptom in allSymptoms:
#         file_writer.writerow(symptom)
