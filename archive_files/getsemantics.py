#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

url = 'https://cs.socmedica.com/api/umkb/getsemanticnewbigid'
#url = 'https://cs.socmedica.com/api/umkb/getsemantic'

param = {'key':'6a1eb6fa9dd973ac',
        'lib':[25],
        'level': 1502,
        'deep': 2,
        'text':'Саркоидоз'
}


response = requests.post(url, param)
outs = response.json()
print(outs)

conceptName2 = []
#conceptName1 = []
#conceptId = []
#conceptCh = []

for out in outs['names'].values():
        print(out)
        #print(out['idConcept'])
        # print(out['id'])
        #print(out['chance'])
        conceptName2.append(out)
        #conceptName1.append(out)
        #conceptId.append(out['idConcept'])
        #conceptCh.append(out['chance'])


print(len(conceptName2))
print(conceptName2)
#print(len(conceptName1))
#print(conceptName1)