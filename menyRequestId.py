#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv
import time

"""Получения перечня концептов по API для получения смысловых графов.
   Получение списка связанных симптомов по id заболеваний и синдромов.
   lib: 25
   ######################################################################################
   level: 1502 
   ######################################################################################
    {
        id - индекс элемента графа. 
        type - тип элемента графа: 0 - индетефицированный элемент запроса; 1 - результат ответа; 2 - результат ответа сформированный инструментом бинаризации.
        nodetype - тип графа(ноды) 0 - ребро; 1 - вершина;
        deep - глубина элемента графа
        parent_id - индекс родительского графа, если есть. 
        level - индекс предиката (связи) или типа концепта
        route - направление связи: 1 - слево на право (ida → idb); 2 - справо на лево (ida ← idb), 3 - двусторонняя связь (id_a <→ id_b)), 0 - неориентированный граф (связь без направления)
        ida - индекс левого плеча. (В новом API этот тип.
        levela - тип концепта левого плеча
        idb - индекс правого плеча. (В новом API этот тип.
        levelb - тип концепта правого плеча
        value_a - вес ребра
        value_b - дополнительное значение ребра (суть значения определяет инструмент онтологии)
        value_c - дополнительное значение ребра (суть значения определяет инструмент онтологии)
        value_d - степень доказательности веса
        sort - индекс сортировки между ребрами графа по приоритету.
    } 
    #####################################################################################  
"""
print('Начало загрузки данных из файла')
tic = time.perf_counter()
url = 'https://cs.socmedica.com/api/umkb/getsemanticnewbigid'
_lib = 25
nosology = []


with open('db/diag_syn_sym_id/syndrome.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f, delimiter=',', )
    for line in reader:
        nosology.append(line['id'])
print('Конец загрузки данных из файла')
print('*'*100)
print('Начало запросов в UMKB')
# print(nosology)
# print(len(nosology))

# for el in nosology:
#     print(el)

nosology = [int(id)*10000 + _lib for id in nosology]
print(nosology)
print(len(nosology))


param = {'key': '6a1eb6fa9dd973ac',
         'lib': [_lib],
         'level': 1502,
         'deep': 10,
         'libid': nosology,
         'route': 0,
         }

# nat_json = json.dumps(param)
# headers = {'Content-type': 'application/json'}

response = requests.post(url, param)
outs = response.json()
#print(outs)

symptoms = outs['graph']
symptoms_names = outs['names']
# allSymptoms.append(symptoms)
# allSymptoms_names.append(symptoms_names)

print('Конец запросов в UMKB')
print('*'*100)
# print(symptoms)
print(len(symptoms))
print(len(symptoms_names))


fieldnames = ['id', 'type', 'nodetype', 'deep', 'parent_id', 'level', 'route', 'ida', 'levela', 'idb', 'levelb',
              'value_a', 'value_b', 'value_c', 'value_d', 'sort']
with open('db/dataset_black/syndrome_symptoms.csv', mode='w', encoding='utf-8', newline='') as file:
    file_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
    file_writer.writeheader()
    for el in symptoms:
        file_writer.writerow(el)


with open('db/dataset_black/syndrome_symptoms_names.csv', mode='w', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id_symptoms', 'name_symptoms'])
    for key, value in symptoms_names.items():
        file_writer.writerow([key, value])



toc = time.perf_counter()
print('Конец работы')
print(f"Вычисление заняло {toc - tic:0.4f} секунд")