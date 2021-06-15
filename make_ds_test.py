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
#
# for symptom_i in symptoms:
#     if type(symptom_i[2]) == list:
#         for symptom_j in symptom_i[2]:
#             for symptom_z in symptoms:
#                 if symptom_i[0] == symptom_z[0]:
#                     if symptom_j == symptom_z[2]:
#                         del symptom_i[3][symptom_i[2].index(symptom_j)]
#                         del symptom_i[2][symptom_i[2].index(symptom_j)]
#
#
# for sym in symptoms_2:
#     for sym2 in symptoms_2:
#         if (sym[0] == sym2[0]):
#             if (sym[2] == sym2[2]):
#                 del symptoms_2[symptoms_2.index(sym2)]
