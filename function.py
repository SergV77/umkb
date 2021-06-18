from settings import *


#Загрузка датасета
def open_file(name):
    """
    Открытие файлов
    :param name: путь к файлу
    :return: возврат списка данных
    """
    with open(name, mode='r', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        symptoms = [[value for value in item.values()] for item in file_reader]
    return symptoms

#Сохранение готового датасета
def save_dataset(name, dataset, fieldnames=['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']):
    with open('db/diag_sym_for_model3.csv', mode='a', encoding='utf-8', newline='') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(fieldnames)
        for key, value in dataset.items():
            for el in list(set(value)):
                file_writer.writerow([key[0], key[1], el[0], el[1]])
    return "Файл сохранен"


#Получения по id список наименований и их синонимов, в том числе на английском языке,
# в виде кортежа name и lang
def get_name_with_base(id, base):
    return ((el[5], el[3]) for el in base if id == int(el[2]))


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