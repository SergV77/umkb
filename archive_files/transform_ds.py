import csv
import string
string.punctuation


"""Проверка на совпадение названий диагнозов-симптомов и их изменение"""
#Загрузка датасета
with open('db/diag_sym_third.csv', mode='r', encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=',')
    symptoms = [[value for value in item.values()] for item in file_reader]

#Раскрываем вложенные списки до первого уровня
def extract_list(item):
    res = []
    for el in item:
        if type(el) == list:
            res += extract_list(el)
        else:
            res += [el]
    return res

#Удаляем не нужные символы
def clean_word(item):
    for p in string.punctuation:
        if p in item:
            item = item.replace(p, '')
    return item.strip()


#Проверка названий и id симптомов и заболеваний на совпадение
#Замена совподающего симптома на симптомы совподающего с названием заболевания
for symptom_i in symptoms:
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


#Сохранение готового датасета
with open('db/diag_sym_for_model3.csv', mode='a', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms'])
    for key, value in symptom_dict.items():
        for el in list(set(value)):
            file_writer.writerow([key[0], key[1], el[0], el[1]])
