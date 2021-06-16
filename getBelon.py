#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import csv

"""Получения перечня концептов по API для получения таблиц с белонами (Раздела) по фильтру.
   Получение списка id заболеваний, синдромов и симптомов.
   lib: 25
   #######################################################################################
   level:
           Заболевания: 185
   Заболевания/Синдром: 184
    Группы заболеваний: 183
              Синдромы: 919
              Симптомы: 920, 930, 1102, 1104 
    ######################################################################################
    {
        id: Идентификационный номер концепта или связи
        master_parent: Старший родитель (по большей части не используется)
        parent_id: Физический родитель (используется для формирования дерево)
        depth: Глубина в дереве (по большей части не используется)
        sort: Порядковый номер среди своего поколения (используется для формирования дерево)
        level: Тип связи или концепта
        nature: не используется
        code: Код концепта
        lib_a: Номер таблицы концепта левого плеча
        id_a: ID концепта левого плеча
        lib_b: Номер таблицы концепта правого плеча
        id_b: ID концепта правого плеча
        sex:  не используется
        value_a: Значение a
        value_b: Значение b
        value_c: Значение c
        value_d: Значение d
        ratio: не используется
        confirmed: не используется
        count: Счетчик (популярность)
        flag: Флаг
    } 
##########################################################################################   
"""
url = 'https://cs.socmedica.com/api/umkb/GetBelWhere'


param = {
        "key": "390ee73a9dccee30",
        "lib": 25,
        "Filtrs": {
                "level": [
                    "920",
                    "930",
                    "1102",
                    "1104"
                ]
        }
}

nat_json = json.dumps(param)
headers = {'Content-type': 'application/json'}

response = requests.post(url, nat_json, headers=headers)
outs = response.json()


fieldnames = ['id', 'master_parent', 'parent_id', 'depth', 'sort', 'level', 'nature', 'code', 'lib_a', 'id_a',
 'lib_b', 'id_b', 'sex', 'value_a', 'value_b', 'value_c', 'value_d', 'ratio', 'confirmed', 'count', 'flag']

with open('db/diag_syn_sym/symptoms.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.DictWriter(file,  delimiter=',', fieldnames=fieldnames)
    file_writer.writeheader()
    for el in outs['Result']:
        file_writer.writerow(el)
