#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv
import time


print('Начало загрузки файла - diagnosis4.csv')
tic = time.perf_counter()
url = 'https://cs.socmedica.com/api/umkb/getsemanticnewbigid'
_lib = 25
nosology = []
# allSymptoms = []


# with open('diagnosis4.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     for line in reader:
#         nosology.append(line['id'])
print('Конец загрузки файла - diagnosis4.csv')
print('*'*100)
print('Начало запросов в UMKB')

# nosology = [int(id)*10000 + _lib for id in nosology]
# print(len(nosology))
#
# for nos in nosology:
#     symptoms = []
param = {'key': '6a1eb6fa9dd973ac',
         'lib': [_lib],
         'level': 1502,
         'deep': 1,
         'libid': [32420025],
         'route': 0,
         }

response = requests.post(url, param)
outs = response.json()
print(outs)
# symptoms.append(outs['names'])
# allSymptoms.append(symptoms)


print('Конец запросов в UMKB')
print('*'*100)
# print(len(allSymptoms))
print('Сохранение результата в файл - diagnosis8.csv')
#
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

# fieldnames = ['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']
# with open('diagnosis6.csv', mode='w', encoding='utf-8', newline='') as file:
#     file_writer = csv.DictWriter(file, fieldnames=fieldnames)
#     file_writer.writeheader()
#     for k, v in allSymptoms.items():
#         file_writer.writerow({'id_diagnosis': k, 'name_diagnosis':v, 'id_symptoms', 'name_symptoms': v})
# fieldnames = ["alerts", "graph", "names", "levels", "keygraph"]
# with open('diagnosis7.csv', mode='w', encoding='utf-8') as file:
#     file_writer = csv.DictWriter(file, fieldnames=fieldnames)
#     file_writer.writerow(outs)
#


toc = time.perf_counter()
print('Конец работы')
print(f"Вычисление заняло {toc - tic:0.4f} секунд")