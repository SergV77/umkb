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

dis_syn_sym_names = open_file('db/dataset_black/disease_syndrome_symptoms_names.csv')
dis_syn_sym_all = open_file('db/dataset_black/disease_syndrome_symptoms.csv')

syn_sym_names = open_file('db/dataset_black/syndrome_symptoms_names.csv')
syn_sym_all = open_file('db/dataset_black/syndrome_symptoms.csv')


#Заболевания
dis_sym_dis = open_file('db/diag_syn_sym_id/disease.csv')

dis_syn = open_file('db/diag_syn_sym_id/disease_syndrome.csv')

syn = open_file('db/diag_syn_sym_id/syndrome.csv')

sym = open_file('db/diag_syn_sym_id/symptoms.csv')

base_25lib = open_file('db/diag_syn_sym_names/conceptLib25.csv')


""" Сделано по заболеваниям"""
print('~' * 550)
print('Получено: ')
#Заболеваний
#Получение синонимов заболеваний
diagnosis = getGroupSynonims(dis_sym_dis, base_25lib)
print('Количество заболеваний -', len(diagnosis))
len_diag = len(diagnosis)

#Заболеваний-синдромов
diagnosis_syndroms = getGroupSynonims(dis_syn, base_25lib)
print('Количество заболеваний-синдромов -', len(diagnosis_syndroms))
len_dig_syn = len(diagnosis_syndroms)

#Синдромов
syndroms = getGroupSynonims(syn, base_25lib)
print('Количество синдромов -', len(syndroms))
len_syn = len(syndroms)

#Симптомов
symptoms = getGroupSynonims(sym, base_25lib)
print('Количество симптомов -', len(symptoms))
len_sym = len(symptoms)
print('Проведение запросов на наличие симптомов')

"""Сделано по симптомам"""

#####################################################################
#Проверка количества пройденных запросов
#Заболеваний
count_diag = countRequest(diagnosis, dis_sym_all)
dis_sym_temp = getDisease(dis_sym_all)
print(dis_sym_all)
dis_sym_id = getSymptos(dis_sym_temp)
print(f'Запрошено {count_diag} заболеваний')
calculat(dis_sym_all, count_diag)
print('~' * 550)
dis_sym_result = getNamesResult(dis_sym_id, dis_sym_names, diagnosis)
print('Количество строк - ', len(dis_sym_result))
temp_x = []
for el in dis_sym_result:
    temp_x.append(el[2])
print('Количество уникальных значений до обработки - ', len(set(temp_x)))
big_dict = makeDictNosology(dis_sym_result)


#Заболеваний-синдромов
count_diag_syn = countRequest(diagnosis_syndroms, dis_syn_sym_all)
print(f'Запрошено {count_diag_syn} заболеваний-синдромов')
dis_syn_sym_cal, dis_syn_have_sym = calculat(dis_syn_sym_all, count_diag_syn)
dis_syn_sym_temp = getDisease(dis_syn_sym_all)
unic_dis_syn = unicDis(dis_syn_sym_temp)
dis_syn_sym_id = getSymptos(dis_syn_sym_temp)
unic_dis_syn_id = unicDis(dis_syn_sym_id)
temp_missed = tempMiised(unic_dis_syn, unic_dis_syn_id)
add_dis_syn_sym = addMissedId(dis_syn_sym_all, temp_missed)
dis_syn_sym_id_missed = getSymptosMissed(add_dis_syn_sym)
dis_syn_sym_id += dis_syn_sym_id_missed
dis_syn_sym_result = getNamesResult(dis_syn_sym_id, dis_syn_sym_names, diagnosis_syndroms)
temp_dict = makeDictNosology(dis_syn_sym_result)

###########################################################################################

#Сохранение готового датасета
with open('db/dataset_white/disease_syndrom_symptoms.csv', mode='a', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms', 'weight'])
    for key, value in temp_dict.items():
        for k, v in value.items():
            file_writer.writerow([*(key), *(k), summ_list(v)])


print(f'Датасет загружен')

##################АРХИВНЫЕ ВЕРСИИ СКРИПТОВ#################################################
###########################################################################################
# print(dis_syn_have_sym)
# dis_syn_sym_temp = getDisease(dis_syn_have_sym)
# dis_syn_sym_id = getSymptos(dis_syn_sym_temp)
# dis_syn_sym_result = getNamesResult(dis_syn_sym_id, dis_syn_sym_names, diagnosis_syndroms)
# print('1~', len(dis_syn_sym_all), dis_syn_sym_all[:2])
# print('2~', len(dis_syn_have_sym), dis_syn_have_sym[:2])
# print('~' * 550)
# print('~' * 550)

# for el in dis_syn_have_sym[:50]:
#     print(el)
# temp_dis_syn_have_sym = []
# for key, value in dis_syn_have_sym.items():
#     print(value)
#     temp_dis_syn_have_sym += getDisease(value)
#
#
# print(temp_dis_syn_have_sym)
# print(len(temp_dis_syn_have_sym))
# for el in temp_dis_syn_have_sym:
#     print(el)
#


###########################################################################################
# print('Количество строк - ', len(dis_syn_sym_result))
# temp_x = []
# for el in dis_syn_sym_result:
#     temp_x.append(el[2])
#
# print('Количество уникальных значений до обработки - ', len(set(temp_x)))
#
# big_dict = makeDisSym(dis_syn_sym_result)
# for key, value in big_dict.items():
#    print(key, ' - ', len(value), ' - ', value)

#
# temp_x = []
# for el in dis_syn_sym_result:
#     temp_x.append(el[2])
# print('Количество уникальных значений до обработки - ', len(set(temp_x)))
# big_dict = makeDisSym(dis_syn_sym_result)
# for key, value in big_dict.items():
#    print(key, ' - ', len(value), ' - ', value)
#
# a = []
# for key in big_dict.keys():
#     a.append(key)
# print(len(a))
#
# #Синдромов
# count_syn = countRequest(syndroms, syn_sym_all)
# syn_sym_temp = getDisease(syn_sym_all)
# syn_sym_id = getSymptos(syn_sym_temp)
# print(f'Запрошено {count_syn} синдромов')
# calculat(syn_sym_all, count_syn)
# print('~' * 550)
# print('~' * 550)
# syn_sym_result = getNamesResult(syn_sym_id, syn_sym_names, syndroms)





#




"""АРХИВИРОВАНО В СВЗИ С ОТСУТСВИЕМ ДАННЫХ"""
"""
#Групп заболеваний
# dis_group_sym_names = open_file('db/dataset_black/disease_group_symptoms_names.csv')
# dis_group_sym_all = open_file('db/dataset_black/disease_group_symptoms.csv')
# dis_group = open_file('db/diag_syn_sym_id/disease_group.csv')
# group_diagnosis = getGroupSynonims(dis_group, base_25lib)
# print('Количество групп заболеваний -', len(group_diagnosis))
# len_gr_diag = len(group_diagnosis)
#Групп заболеваний
# count_group_diag = countRequest(group_diagnosis, dis_group_sym_all)
# dis_group_sym_temp = getDisease(dis_group_sym_all)
# dis_group_sym_id = getSymptos(dis_group_sym_temp)
# dis_group_sym_result = getNamesResult(dis_group_sym_id, dis_group_sym_names, group_diagnosis)
# print('Количество запросов групп заболеваний -', count_group_diag)


# for el in big_block.items():
#     print(el)
#     print('Глубина выборки ', el[0])
#     count_k = 0
#     count_v = 0
#     for k, v in el[1].items():
#         count += len(v)
#         count_k += 1
#         count_v += len(v)
#         print(k, ' - ', v)
#         print('Количество симптомов - ', len(v))
#         print('~'*550)
#     print('~' * 550)
#     print('ИТОГО:')
#     print('Количество диагнозов на уровне ', count_k)
#     print('Количество симптомов на уровне ', count_v)
#     print('~' * 550)
#
#
# print(len(big_block), count)
"""
# #Заболеваний-синдромов
# count_diag_syn = countRequest(diagnosis_syndroms, dis_syn_sym_all)
# print(f'Запрошено {count_diag_syn} заболеваний-синдромов')
# dis_syn_sym_cal, dis_syn_have_sym = calculat(dis_syn_sym_all, count_diag_syn)
# ###########################################################################################
# dis_syn_sym_temp = getDisease(dis_syn_sym_all)
# temp0 = []
# temp1 = []
# for el in dis_syn_sym_temp:
#     if el[3] == '1':
#         temp0.append(el)
#         temp1.append(el[0])
# print('~' * 550)
#
# dis_syn_sym_id = getSymptos(dis_syn_sym_temp)
# temp2 = []
# for el1 in dis_syn_sym_id:
#     if el1[3] == '1':
#         temp2.append(el1[0])
# print('~' * 550)
#
# temp_missed = []
# for el in set(temp1):
#     if el not in set(temp2):
#         temp_missed.append(el)
#
# temp3 = []
#
# for el1 in getDisease(dis_syn_sym_all):
#     if el1[3] == '1':
#         if el1[0] in temp_missed:
#             temp3.append(el1)
#     else:
#         temp3.append(el1)
#
# dis_syn_sym_id_missed = getSymptosMissed(temp3)
# dis_syn_sym_id += dis_syn_sym_id_missed
# temp5 = []
# for el in dis_syn_sym_id:
#     temp5.append(el[0])
# print(len(set(temp5)))
#
# dis_syn_sym_result = getNamesResult(dis_syn_sym_id, dis_syn_sym_names, diagnosis_syndroms)
# big_dict = makeDisSym(dis_syn_sym_result)
#
#
# for key, value in big_dict.items():
#    print(key, ' - ', len(value), ' - ', value)
# #
# print(len(big_dict))
