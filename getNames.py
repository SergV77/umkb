#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

"""Получения перечня концептов по API для выгрузки библиотеки с названиями концептов - LibNames.
   Получение списка наименований заболеваний, синдромов и симптомов.
   lib: 25 
   id (uint) - идентификационный номер записи
   master_id (uint) - идентификационный номер концепта
   lang (string) - язык на котором представлено название концепта
   field (string) - тип названия концепта (name, short, adational, old)
   text (string) - название концепта
   weight (byte) - вес (0 - основное название, 1>= синоним)       
"""
url = 'https://cs.socmedica.com/api/umkb/unloadingLibNames'


param = {
    "permit": {
        "key": "b1b7677fd188dd43"
    },
    "lib": 25
}

nat_json = json.dumps(param)
headers = {'Content-type': 'application/json'}

response = requests.post(url, nat_json, headers=headers)
outs = response.json()


fieldnames = ['lib', 'id', 'master_id', 'lang', 'field', 'text', 'weight', 'popularity']

with open('db/diag_syn_sym_names/conceptLib25.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.DictWriter(file,  delimiter=',', fieldnames=fieldnames)
    file_writer.writeheader()
    for el in outs:
        file_writer.writerow(el)
