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

#Удаляем не нужные символы
def clean_word(item):
    for p in string.punctuation:
        if p in item:
            item = item.replace(p, '')
    return item.strip()

#Раскрываем вложенные списки до первого уровня
def extract_list(item):
    res = []
    for el in item:
        if type(el) == list:
            res += extract_list(el)
        else:
            res += [el]
    return res

#Раскрываем вложенные списки до первого уровня
def summ_list(item):
    return round(sum(float(el) ** 2 for el in item if el != '' and el != '-0.9' ) / len(item), 4)


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

#Расссчет результатов загрузки
def calculat(base, count):
    big_block = {}
    big_list = {}
    for el in base:
        block_idb = []
        block_ida = []
        if el[3] == '0':
            for sym in base:
                if sym[3] == '1':
                    if el[0] == sym[7]:
                        block_idb.append(sym[9])
                        block_ida.append(sym)
                if len(block_idb) > 0:
                    big_block[el[0]] = block_idb
                    big_list[el[0]] = block_ida


    count_k = 0
    count_v = 0
    for k, v in big_block.items():
        count_k += 1
        count_v += len(v)
        #print(k, ' - ', v)
        #print('Количество непосредственных симптомов - ', len(v))
    print('Общее количество диагнозов имеющих симптомы', count_k)
    print('Общее количество диагнозов не имеющие симптомов', count - count_k)
    print('Общее количество непосредственных симптомов', count_v)
    return big_block, big_list



#Получение заболеваний (синдромов) и связанных с ними симптомов
def getDisease(base):
    big_block = []
    for el in base:
        if el[3] != '0':
            big_block.append([el[7], el[9], el[11], el[3]])

    return big_block


# Свертка симптомов с последнего уровня на первый
def getSymptos(base):
    parant_list = []
    child_list = []
    temp_list = []
    weight = []
    temp_weight = []

    for el in base:
        if el[0] not in child_list:
            temp_list.append(el)
            parant_list.append(el[0])
            child_list.append(el[1])
            weight.append(el[2])
        else:
            temp_weight.append(el[2])
            temp_weight.append(weight[child_list.index(el[0])])
            el[0] = parant_list[child_list.index(el[0])]
            el[2] = summ_list(extract_list(temp_weight))
            temp_list.append(el)
            child_list.append(el[1])
            parant_list.append(el[0])
            weight.append(el[2])
            temp_weight = []

    return temp_list

def getSymptosMissed(base):
    parant_list = []
    child_list = []
    temp_list = []
    weight = []
    temp_weight = []

    for el in base:
        if el[3] == "1":
            if el[0] not in child_list:
                temp_list.append(el)
                parant_list.append(el[0])
                child_list.append(el[1])
                weight.append(el[2])
        else:
            if el[0] not in child_list:
                continue
            else:
                temp_weight.append(el[2])
                temp_weight.append(weight[child_list.index(el[0])])
                el[0] = parant_list[child_list.index(el[0])]
                el[2] = summ_list(extract_list(temp_weight))
                temp_list.append(el)
                child_list.append(el[1])
                parant_list.append(el[0])
                weight.append(el[2])
                temp_weight = []

    return temp_list

#Получение название заболевания
def getNameDys(_id, items):
    name = ''
    for el in items:
        if _id == str(el[0]):
            name = el[1][0][0]
    return name

#Получение название симптома
def getNameSym(_id, base_names):
    name = ''
    for el in base_names:
        if _id == el[0]:
            name = el[1]
    return name

#Получение название заболевания и симптомов
def getNamesResult(base_id, base_names, items):
    result = []
    for _id in base_id:
        name1 = getNameDys(_id[0], items) #Получение название заболевания
        name2 = getNameSym(_id[1], base_names) #Получение название симптома
        result.append([_id[0], clean_word(name1), _id[1], clean_word(name2), _id[2]])

    return result


def unicDis(base):
    temp = []
    for el in base:
        if el[3] == '1':
            temp.append(el[0])
    return temp

#Проверка на не учтенные id
def tempMiised(base, base_id):
    temp_missed = []
    for el in set(base):
        if el not in set(base_id):
            temp_missed.append(el)
    return temp_missed

#Добавление не учтенных id
def addMissedId(base, temp_missed):
    temp = []
    for el in getDisease(base):
        if el[3] == '1':
            if el[0] in temp_missed:
                temp.append(el)
        else:
            temp.append(el)
    return temp

#Группирует заболевания и убирает дублирующие симптомы
#с сохранением весов
def makeDictNosology(base):
    temp_dict = {}
    for el in base:
        if (el[0], el[1]) not in temp_dict.keys():
            temp_dict[(el[0], el[1])] = [(el[2], el[3], el[4])]
        else:
            temp_dict[(el[0], el[1])].append((el[2], el[3], el[4]))

    for key, value in temp_dict.items():
        small_dict = {}
        for el in value:
            if (el[0], el[1]) not in small_dict.keys():
                small_dict[(el[0], el[1])] = [el[2]]
            else:
                small_dict[(el[0], el[1])].append(el[2])

        temp_dict[key] = small_dict

    return temp_dict




# удаление дублирующих симптомов
# с сохранением среднего веса
# def delDoublName(base):
#     small_dict = {}
#     for el in base:
#         weight = []
#         for sym in base:
#             if el[0] == sym[0]:
#                 if el[2] == sym[2]:
#                     weight.append(sym[4])
#         small_dict[(el[2], el[3])] = summ_list(weight)
#     return small_dict
#
# # Создание словаря заболевания - симптомы
# def makeDisSym(base):
#     big_dict = {}
#     for el in {(el[0], el[1]) for el in base}:
#         for sym in {(el[0], el[1]) for el in base}:
#             if el[0] == sym[0]:
#                 big_dict[el] = delDoublName(base)
#     return big_dict

#Функции в разработке
def makeGroupSymptoms(item, base):
    group_sym = []
    for sym in base:
        if item == sym[7]:
            group_sym.append(makeGroupSymptoms(sym[9], base))
    return group_sym

def prepareGroup(base):
    big_block = {}
    for el in base:
        block_idb = []
        if el[3] == '0':
            for sym in base:
                if sym[3] == '1':
                    if el[0] == sym[7]:
                        block_idb.append(sym[9])
            if len(block_idb) > 0:
                block_temp = []
                for e in block_idb:
                    concept = makeGroupSymptoms(e, base)
                    if len(concept) != 0:
                        block_temp.append(concept)
                    else:
                        block_temp.append(e)
                big_block[el[0]] = block_temp

    return big_block


# Архив
# # Свертка симптомов с последнего уровня на первый
# def getSymptos(base):
#     parant_list = []
#     child_list = []
#     temp_list = []
#     weight = []
#     temp_weight = []
#
#     for el in base:
#         if el[0] not in child_list:
#             temp_list.append(el)
#             parant_list.append(el[0])
#             child_list.append(el[1])
#             weight.append(el[2])
#         else:
#             temp_weight.append(el[2])
#             temp_weight.append(weight[child_list.index(el[0])])
#             el[0] = parant_list[child_list.index(el[0])]
#             el[2] = summ_list(extract_list(temp_weight))
#             temp_list.append(el)
#             child_list.append(el[1])
#             parant_list.append(el[0])
#             weight.append(el[2])
#             temp_weight = []
#
#     return temp_list

# def getSymptos(base):
#     parant_list = []
#     child_list = []
#     temp_list = []
#     weight = []
#     temp_weight = []
#
#     for el in base:
#         if el[3] == "1":
#             if el[0] not in child_list:
#                 temp_list.append(el)
#                 parant_list.append(el[0])
#                 child_list.append(el[1])
#                 weight.append(el[2])
#         else:
#             if el[0] not in child_list:
#                 continue
#             else:
#                 temp_weight.append(el[2])
#                 temp_weight.append(weight[child_list.index(el[0])])
#                 el[0] = parant_list[child_list.index(el[0])]
#                 el[2] = summ_list(extract_list(temp_weight))
#                 temp_list.append(el)
#                 child_list.append(el[1])
#                 parant_list.append(el[0])
#                 weight.append(el[2])
#                 temp_weight = []
#
#     return temp_list