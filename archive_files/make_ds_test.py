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



#
# def collection_symptoms(item):
#     result = []
#     for el in dis_sym_all:
#         if item == el[7]:
#             result.append(collection_symptoms(el[9]))
#
#     if len(result) != 0:
#         return result
#     else:
#         return item
#
# sym_dict = {}
# for sym in dis_sym_all:
#     ida = []
#     if int(sym[3]) == 0:
#         for el in dis_sym_all:
#             if sym[0] == el[7]:
#                 ida.append(collection_symptoms(el[9]))
#         sym_dict[sym[0]] = ida
#


#
# print(sym_dict)

# def collection_symptoms(item):
#     result = {}
#     for sym in dis_sym_all:
#         idb = []
#         for el in dis_sym_all:
#             if sym[9] == el[7]:
#                 idb.append[collection_symptomssym[9]]
#         result[sym[7]] = idb
#     return result



# for k, v in big_block.items():
#     print(k, ' - ', v)
# print(len(big_block))
#
# print(big_block)
# for el in info_diag:
#     print(el)


# def get_big_id(id):
#     return ((int(el[0]) * 10000 + 25 for el in dis_sym_dis))
#

# print(len(dis_sym_dis))
#Преобразование id в newBigId
#
# print(newBigId)
# print(len(newBigId))

#newBigId = [int(id)*10000 + 25 for id in newBigId]



#
# for el in dis_sym_names:
#     print(el)
# print(len(dis_sym_names))

# for el in dis_sym_names[0]:
#     print(dis_sym_all)

# fieldnames=['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']


#
# for el in dis_sym_names:
#     print(el)
# print(len(dis_sym_names))
#
# def makeGroupSymptoms(item, base):
#     group_sym = []
#     for sym in base:
#         if item == sym[7]:
#             group_sym.append(makeGroupSymptoms(sym[9], base))
#     return group_sym
#
#
# def prepareGroup(base):
#     big_block = {}
#     for el in base:
#         block_idb = []
#         if el[3] == '0':
#             for sym in base:
#                 if sym[3] == '1':
#                     if el[0] == sym[7]:
#                         block_idb.append(sym[9])
#             if len(block_idb) > 0:
#                 block_temp = []
#                 for e in block_idb:
#                     concept = makeGroupSymptoms(e, base)
#                     if len(concept) != 0:
#                         block_temp.append(concept)
#                     else:
#                         block_temp.append(e)
#                 big_block[el[0]] = block_temp
#
#     return big_block
#
#
# print(prepareGroup(dis_sym_all))



#
# big_block = {}
# for el in dis_sym_all:
#     block_idb = []
#     if el[3] == '0':
#         for sym in dis_sym_all:
#             if sym[3] == '1':
#                 if el[0] == sym[7]:
#                     block_idb.append(sym[9])
#             for el in block_idb:
#                 small_block = []
#                 for sym in dis_sym_all:
#                     if el == sym[7]:
#                         small_block.append(sym[9])
#                 block_temp.append(small_block)
#             big_block[el[0]] = block_idb
#
# print(big_block)

"""
#Проверка названий и id симптомов и заболеваний на совпадение
#Замена совподающего симптома на симптомы совподающего с названием заболевания
for symptom_i in symptoms_names:
    sym_name = [symptom_j[3] for symptom_j in symptoms if symptom_i[2] == symptom_j[0]]
    sym_id = [symptom_j[2] for symptom_j in symptoms if symptom_i[2] == symptom_j[0]]


    if len(sym_id) != 0:
        symptom_i[2] = (extract_list(sym_id))
        symptom_i[3] = (extract_list(sym_name))


#Извлечение симптомов из одной строки по нескольким строкам,
#согласно их диагнозам
symptoms_2 = []
for sym in symptoms:
    if type(sym[2]) == list:
        for i in range(len(sym[2])):
            symptoms_2.append([sym[0], sym[1], sym[2][i], clean_word(sym[3][i])])
    else:
        symptoms_2.append([sym[0], sym[1], sym[2], clean_word(sym[3])])


#Группировка id диагнозов и симптомов с их названием в кортежи
list_sym = []
for sym in symptoms_2:
    list_sym.append(((int(sym[0]), sym[1]), (int(sym[2]), sym[3])))

#Группировка кортежей диагнозов
#и их очистка от дубликатов
diagnosys_list = []
for el in list_sym:
    diagnosys_list.append(el[0])

diagnosys_list = list(set(diagnosys_list))


#Составление словаря дигнозов и списка их симптомов
symptom_dict = {}
for el in diagnosys_list:
    temp_list = []
    for sym in list_sym:
        if el == sym[0]:
            temp_list.append(sym[1])
    symptom_dict[el] = temp_list


"""