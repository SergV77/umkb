import csv
import string
string.punctuation

symptoms = []
fieldnames = ['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']
with open('diagnosis8.csv', mode='r', encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=',')
    for item in file_reader:
        symptoms.append([value for value in item.values()])

#Раскрываем вложенный списки до первого уровня
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


for sym1 in symptoms:
    sym_name = [sym2[3] for sym2 in symptoms if sym1[2] == sym2[0]]
    sym_id = [sym2[2] for sym2 in symptoms if sym1[2] == sym2[0]]

    if len(sym_id) != 0:
        sym1[2] = extract_list(sym_id)
        sym1[3] = extract_list(sym_name)



with open('diagnosis11.csv', mode='a', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
    file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms'])
    for sym in symptoms:
        if type(sym[2]) == list:
            tmp_sym = [i for i in zip(sym[2], sym[3])]
            for i in range(len(tmp_sym)):
                """Скорректировать проверку на дубликаты"""
                # for
                # if tmp_sym[i][0] != tmp_sym[i][0]:
                #     file_writer.writerow([sym[0], sym[1], tmp_sym[i][0], clean_word(tmp_sym[i][1])])

        else:
            file_writer.writerow([sym[0], sym[1], sym[2], clean_word(sym[3])])
