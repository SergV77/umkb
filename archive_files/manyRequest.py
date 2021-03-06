#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

url = 'https://cs.socmedica.com/api/umkb/getsemanticnewbigid'
#url = 'https://cs.socmedica.com/api/umkb/getsemantic'

print('Начало загрузки файла - diagnosis4.csv')
nosology = []
# with open('diagnosis4.csv', 'r', encoding='utf-8') as f:
#     load_file = csv.reader(f)
#     for row in load_file:
#         nosology.append(row)

with open('diagnosis.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        nosology.append(line['id'])
print('Конец загрузки файла - diagnosis4.csv')
print('*'*100)
print('Начало запросов в UMKB')

allSymptoms = []
for word in nosology[0]:

    symptoms = []
    param = {'key': '6a1eb6fa9dd973ac',
             'lib': [25],
             'level': 1502,
             'deep': 1,
             "libid": [],
             "route": 0,
             }


    response = requests.post(url, param)
    outs = response.json()

    if outs['names'] == None:
        continue
    else:
        for out in outs['names'].values():
            symptoms.append(out)

    if len(symptoms) != 0:
        allSymptoms.append(symptoms)

print('Конец запросов в UMKB')
print('*'*100)
print(len(allSymptoms))
print('Сохранение результата в файл - diagnosis2.csv')

with open('diagnosis2.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    for symptom in allSymptoms:
        file_writer.writerow(symptom)

print('Конец работы')

# print('Сохранение результата в файл - diagnosis8.csv')
# #
# with open('diagnosis8.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms'])
#     for item in allSymptoms:
#         new_dict = {}
#         new_dict[[(k, v) for k, v in item[0].items()][0]] = [(k, v) for k, v in item[0].items()][1:]
#         for k, v in new_dict.items():
#             diagnosis = k
#             symptoms = v
#             for el in symptoms:
#                 file_writer.writerow([diagnosis[0], diagnosis[1], el[0], el[1]])