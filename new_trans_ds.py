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
#
# #Заболеваний-синдромов
# diagnosis_syndroms = getGroupSynonims(dis_syn, base_25lib)
# print('Количество заболеваний-синдромов -', len(diagnosis_syndroms))
# len_dig_syn = len(diagnosis_syndroms)
#
# #Синдромов
# syndroms = getGroupSynonims(syn, base_25lib)
# print('Количество синдромов -', len(syndroms))
# len_syn = len(syndroms)

#Симптомов
# symptoms = getGroupSynonims(sym, base_25lib)
# print('Количество симптомов -', len(symptoms))
# len_sym = len(symptoms)
print('~' * 550)
print('~' * 550)
print('Проведение запросов на наличие симптомов')
print('~' * 550)

"""
В процессе по симптомам
"""

#####################################################################
#Проверка количества пройденных запросов
#Заболеваний
count_diag = countRequest(diagnosis, dis_sym_all)
dis_sym_temp = getDisease(dis_sym_all)
dis_sym_id = getSymptos(dis_sym_temp)
print(f'Запрошено {count_diag} заболеваний')
calculat(dis_sym_all, count_diag)
print('~' * 550)
dis_sym_result = getNamesResult(dis_sym_id, dis_sym_names, diagnosis)

temp_x = []
for el in dis_sym_result:
    temp_x.append(el[2])
print(' до - ', len(set(temp_x)))



count = 0
print(len(dis_sym_result))

big_dict = {}
temp_list = []
for el in dis_sym_result:
    small_dict = {}
    weight = []
    for sym in dis_sym_result:
        if el[0] == sym[0]:
            if el[2] == sym[2]:
                weight.append(sym[4])
    small_dict[(el[2], el[3])] = weight
#big_dict[el[0]] = small_dict


#print(' после - ', big_dict)
#
for k, v in small_dict.items():
   print(k, ' - ', len(v), ' - ', v)

#print(' после - ', len(temp_list))

# temp_y = []
# for el in temp_list:
#     temp_y.append(el[2])
# print(' после2 - ', len(set(temp_y)))
# print([x for x in temp_x if x not in temp_y])
#

#
# #Заболеваний-синдромов
# count_diag_syn = countRequest(diagnosis_syndroms, dis_syn_sym_all)
# dis_syn_sym_temp = getDisease(dis_syn_sym_all)
# dis_syn_sym_id = getSymptos(dis_syn_sym_temp)
# print(f'Запрошено {count_diag_syn} заболеваний-синдромов')
# calculat(dis_syn_sym_all, count_diag_syn)
# print('~' * 550)
# print('~' * 550)
# dis_syn_sym_result = getNamesResult(dis_syn_sym_id, dis_syn_sym_names, diagnosis_syndroms)
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
# #Сохранение готового датасета
# with open('db/dataset_white/disease_symptoms.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms', 'weight'])
#     for el in dis_sym_result:
#         file_writer.writerow(el)
#
# print(f'Датасет загружен')






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