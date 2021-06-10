import csv


lst = ['крапивница и эритема', ['крапивница', 'крапивница и эритема', ['отек', 'ощущение распирания', 'зуд'], 'волдырь'], 'ощущение распирания', 'зуд', 'волдырь']

def extract_list(item):
    res = []
    for el in item:
        if type(el) == list:
            res += extract_list(el)
        else:
            res += [el]
    return res

print(extract_list(lst))

#
# symptoms = []
#
#
# fieldnames = ['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']
# with open('diagnosis8.csv', mode='r', encoding='utf-8') as file:
#     file_reader = csv.DictReader(file, delimiter=',')
#     for item in file_reader:
#         symptom = []
#         for value in item.values():
#             symptom.append(value)
#         symptoms.append(symptom)
#
# test = []
# for i in range(len(symptoms)):
#     for j in range(len(symptoms)):
#         if symptoms[j][2] == symptoms[i][0]:
#             test.append(symptoms[j][2])
#
# test = list(set(test))
# print(test)
# print(len(test))