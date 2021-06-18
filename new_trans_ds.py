from settings import *
from function import *

"""
Формирование датасета из таблиц исходных данных
################################################
#ID заболевания
dis_sym_dis['id']

#NAME заболевания
base_25lib['master_id']
base_25lib['text']

#ID симптома - заболевания
dis_sym_all['id']

#NAME симптома - заболевания
dis_sym_names['id_symptoms']
dis_sym_names['name_symptoms']
###############################################
"""

#Загрузка данных с файлов
#Симптомы по заболеваниям
dis_sym_names = open_file('db/dataset_black/disease_symptoms_names.csv')
dis_sym_all = open_file('db/dataset_black/disease_symptoms.csv')
#Заболевания
dis_sym_dis = open_file('db/diag_syn_sym_id/disease.csv')
base_25lib = open_file('db/diag_syn_sym_names/conceptLib25.csv')


""" Сделано по заболеваниям"""
diagnosis = []
for el in dis_sym_dis:
    diagnosis.append(( int(el[0]) * 10000 + 25, [*get_name_with_base(int(el[0]), base_25lib)] ))

# for el in diagnosis:
#     print(el)

print(len(diagnosis))


"""
В процессе по симптомам
"""
#Проверка количества пройденных запросов
count = 0
for diag in diagnosis:
    for sym in dis_sym_all:
        if int(diag[0]) == int(sym[0]):
            if sym[3] == '0':
                count +=1
print('Количество пройденных запросов - ', count)

big_block = {}
info_diag = []
for sym in dis_sym_all:
    block = []
    for el in dis_sym_all:
        if sym[0] == el[7]:
            block.append(el[0])
            info_diag.append(el)

    if len(block) > 0:
        big_block[sym[0]] = block


def collection_symptoms(item):
    result = []
    for el in dis_sym_all:
        if item == el[7]:
            result.append(collection_symptoms(el[9]))

    if len(result) != 0:
        return result
    else:
        return item

sym_dict = {}
for sym in dis_sym_all:
    ida = []
    if int(sym[3]) == 0:
        for el in dis_sym_all:
            if sym[0] == el[7]:
                ida.append(collection_symptoms(el[9]))
        sym_dict[sym[0]] = ida




print(sym_dict)

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
print(big_block)
for el in info_diag:
    print(el)


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

fieldnames=['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']


#
# for el in dis_sym_names:
#     print(el)
# print(len(dis_sym_names))


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
