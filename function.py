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

#Рассчет количества заболеваний - синдромов - симптомов
def getGroupSynonims(file, base):
    return [(int(el[0]) * 10000 + 25, [*get_name_with_base(int(el[0]), base)]) for el in file]

#Проверка количества пройденных запросов
def countRequest(item, symtoms):
    count = 0
    for diag in item:
        for sym in symtoms:
            if int(diag[0]) == int(sym[0]):
                if sym[3] == '0':
                    count += 1
    return count

def get_block(symtoms):
    big_block = {}
    temp_dict = list({sym[7] for sym in symtoms})
    for el in temp_dict:
        block = []
        for sym in symtoms:
            if el == sym[7]:
                block.append((sym[9], sym[11]))
        big_block[el] = block

    return big_block



def prepareGroup(base):
    big_block = {}
    for el in base:
        block_idb = []
        if el[3] == '0':
            for sym in base:
                if sym[3] == '1':
                    if el[0] == sym[7]:
                        block_idb.append((sym[9], sym[11]))
                if len(block_idb) > 0:
                    big_block[el[0]] = block_idb

    return big_block


# def makeGroupSymptoms(item, base):
#     group_sym = [makeGroupSymptoms(sym[9], base) for sym in base if item == sym[7]]
#     if len(group_sym) > 0:
#         return group_sym
#     else:
#         return item

#
def makeGroupSymptoms(item, base):
    group_sym = []
    for sym in base:
        if item == sym[7]:
            group_sym.append(makeGroupSymptoms(sym[9], base[base.index(sym):]))
    if len(group_sym) > 0:
        return group_sym
    else:
        return item
#
# def prepareGroup(base):
#     big_block = {}
#     for el in base:
#         block_idb = []
#         while el[3] == '0':
#             for sym in base:
#                 while sym[3] == '1':
#                     if el[0] == sym[7]:
#                         block_idb.append(sym[9])
#                 if len(block_idb) > 0:
#                     big_block[el[0]] = block_idb
#
#     return big_block
#
# def get_block(symtoms):
#     big_block = {}
#     temp_dict = list({sym[7] for sym in symtoms})
#
#     for el in temp_dict:
#         block = []
#         for sym in symtoms:
#             print('1 - ', el)
#             print('2 - ', sym)
#             print('4 - ', int(sym[7]))
#             if el == int(sym[7]):
#                 print('3 - ', sym)
#                 block.append((el[9], el[11]))
#                 print(block)
#         if len(block) > 0:
#             print('4 - ', block)
#             big_block[el] = block
#             print('5 - ', big_block)
#
#     return big_block
#
