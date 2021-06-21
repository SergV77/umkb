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
#dis_sym_names = open_file('db/dataset_black/disease_symptoms_names.csv')
dis_sym_all = open_file('db/dataset_black/disease_symptoms.csv')
dis_group_sym_all = open_file('db/dataset_black/disease_group_symptoms.csv')
dis_syn_sym_all = open_file('db/dataset_black/disease_syndrome_symptoms.csv')
syn_sym_all = open_file('db/dataset_black/syndrome_symptoms.csv')


#Заболевания
dis_sym_dis = open_file('db/diag_syn_sym_id/disease.csv')
dis_group = open_file('db/diag_syn_sym_id/disease_group.csv')
dis_syn = open_file('db/diag_syn_sym_id/disease_syndrome.csv')
syn = open_file('db/diag_syn_sym_id/syndrome.csv')
sym = open_file('db/diag_syn_sym_id/symptoms.csv')
base_25lib = open_file('db/diag_syn_sym_names/conceptLib25.csv')


""" Сделано по заболеваниям"""

#Заболеваний
diagnosis = getGroupSynonims(dis_sym_dis, base_25lib)
print('Количество заболеваний -', len(diagnosis))
len_diag = len(diagnosis)
#
# #Групп заболеваний
# group_diagnosis = getGroupSynonims(dis_group, base_25lib)
# print('Количество групп заболеваний -', len(group_diagnosis))
# len_gr_diag = len(group_diagnosis)
#
# #Заболеваний-синдромов
# diagnosis_syndroms = getGroupSynonims(dis_syn, base_25lib)
# print('Количество заболеваний синдромов -', len(diagnosis_syndroms))
# len_dig_syn = len(diagnosis_syndroms)
#
# #Синдромов
# syndroms = getGroupSynonims(syn, base_25lib)
# print('Количество синдромов -', len(syndroms))
# len_syn = len(syndroms)
#
# #Симптомов
# # symptoms = getGroupSynonims(sym, base_25lib)
# # print('Количество симптомов -', len(symptoms))
# # len_sym = len(symptoms)



"""
В процессе по симптомам
"""


#Проверка количества пройденных запросов
#Заболеваний
count_diag = countRequest(diagnosis, dis_sym_all)

deep = {int(sym[3]) for sym in dis_sym_all[count_diag+1:]}
# print(deep)
# print(len(deep))


big_block = []
for i in deep:
    temp_list = []
    for sym in dis_sym_all[count_diag:]:
        if int(sym[3]) == int(i):
            temp_list.append(sym)

    if len(temp_list) > 0:
        big_block.append((i, get_block(temp_list)))


count = 0
for el in big_block:
    print(el[0])
    count_k = 0
    count_v = 0
    for k, v in el[1].items():
        count += len(v)
        count_k += 1
        count_v += len(v)
        print(k, ' - ', v)
        print('Количество симптомов - ', len(v))
        print('~'*550)
    print('~' * 550)
    print('Количество диагнозов на уровне ', count_k)
    print('Количество симптомов на уровне ', count_v)
    print('~' * 550)


print(len(big_block), count)

# #Групп заболеваний
# count_group_diag = countRequest(group_diagnosis, dis_group_sym_all)
# print(count_group_diag)
#
# #Заболеваний-синдромов
# count_diag_syn = countRequest(diagnosis_syndroms, dis_syn_sym_all)
# print(count_diag_syn)
#
# #Синдромов
# count_syn = countRequest(syndroms, syn_sym_all)
# print(count_syn)

#
# groupDiagnosis = prepareGroup(dis_sym_all)
# print(groupDiagnosis)
# for k, v in groupDiagnosis.items():
#     print(v)
#
# new_dict = {}
# for key, value in groupDiagnosis.items():
#     block_temp = []
#     for e in value:
#        block_temp.append(makeGroupSymptoms(e, dis_sym_all))
#     new_dict[key] = block_temp
#
#
#
#
#Сохранение готового датасета
with open('test.csv', mode='a', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id_diagnosis', 'id_symptoms', 'weight', 'deep'])
    for el in big_block:
        for key, value in el[1].items():
            for val in value:
                file_writer.writerow([key, *(val), el[0]])




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
