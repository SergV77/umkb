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
dis_group_sym_names = open_file('db/dataset_black/disease_group_symptoms_names.csv')
dis_group_sym_all = open_file('db/dataset_black/disease_group_symptoms.csv')
dis_syn_sym_names = open_file('db/dataset_black/disease_syndrome_symptoms_names.csv')
dis_syn_sym_all = open_file('db/dataset_black/disease_syndrome_symptoms.csv')
syn_sym_names = open_file('db/dataset_black/syndrome_symptoms_names.csv')
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
#Получение синонимов заболеваний
diagnosis = getGroupSynonims(dis_sym_dis, base_25lib)
print('Количество заболеваний -', len(diagnosis))
len_diag = len(diagnosis)

#Групп заболеваний
group_diagnosis = getGroupSynonims(dis_group, base_25lib)
print('Количество групп заболеваний -', len(group_diagnosis))
len_gr_diag = len(group_diagnosis)

#Заболеваний-синдромов
diagnosis_syndroms = getGroupSynonims(dis_syn, base_25lib)
print('Количество заболеваний синдромов -', len(diagnosis_syndroms))
len_dig_syn = len(diagnosis_syndroms)

#Синдромов
syndroms = getGroupSynonims(syn, base_25lib)
print('Количество синдромов -', len(syndroms))
len_syn = len(syndroms)

#Симптомов
# symptoms = getGroupSynonims(sym, base_25lib)
# print('Количество симптомов -', len(symptoms))
# len_sym = len(symptoms)

print('~' * 550)
print('Запрос симптомов ')
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
dis_sym_result = getNamesResult(dis_sym_id, dis_sym_names, diagnosis)
print('Количество запросов заболеваний -', count_diag)
# for el in dis_sym_result:
#     print(el)

#Групп заболеваний
count_group_diag = countRequest(group_diagnosis, dis_group_sym_all)
dis_group_sym_temp = getDisease(dis_group_sym_all)
dis_group_sym_id = getSymptos(dis_group_sym_temp)
dis_group_sym_result = getNamesResult(dis_group_sym_id, dis_group_sym_names, group_diagnosis)
print('Количество запросов групп заболеваний -', count_group_diag)

#Заболеваний-синдромов
count_diag_syn = countRequest(diagnosis_syndroms, dis_syn_sym_all)
dis_syn_sym_temp = getDisease(dis_syn_sym_all)
dis_syn_sym_id = getSymptos(dis_syn_sym_temp)
dis_syn_sym_result = getNamesResult(dis_syn_sym_id, dis_syn_sym_names, diagnosis_syndroms)
print('Количество запросов заболеваний-синдромов -', count_diag_syn)

#Синдромов
count_syn = countRequest(syndroms, syn_sym_all)
syn_sym_temp = getDisease(syn_sym_all)
syn_sym_id = getSymptos(syn_sym_temp)
syn_sym_result = getNamesResult(syn_sym_id, syn_sym_names, syndroms)
print('Количество запросов синдромов -', count_syn)

#dis_sym_all, dis_group_sym_all, dis_syn_sym_all, syn_sym_all
temp_block = []
big_block = {}
for el in dis_group_sym_all:
    block_idb = []
    if el[3] == '0':
        for sym in dis_group_sym_all:
            if sym[3] == '1':
                if el[0] == sym[7]:
                    block_idb.append(sym[9])
            if len(block_idb) > 0:
                big_block[el[0]] = block_idb
            temp_block.append(big_block)

print(big_block)
# big_block = getDisease(dis_group_sym_all)
#
# for el in big_block:
#     print(el)
#
count = 0
for el in big_block:
    print('Глубина выборки ', el[0])
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
    print('ИТОГО:')
    print('Количество диагнозов на уровне ', count_k)
    print('Количество симптомов на уровне ', count_v)
    print('~' * 550)


print(len(big_block), count)

# #
# #Сохранение готового датасета
# with open('test4.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms', 'weight'])
#     for el in dis_syn_sym_result:
#         file_writer.writerow(el)




