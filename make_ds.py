import csv


symptoms = []

fieldnames = ['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms']
with open('diagnosis8.csv', mode='r', encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=',')
    for item in file_reader:
        symptom = []
        for value in item.values():
            symptom.append(value)
        symptoms.append(symptom)

# summ = 0
# for sym in symptoms:
#     if sym[3].find("'") > 0:
#         summ += int(sym[3].find("'"))
#         print("Запятые :", sym[3].find("'"))
#         print(summ)

for i in range(len(symptoms)):
    tmp_sym_id = []
    tmp_sym_name = []
    for j in range(len(symptoms)):
        if symptoms[i][2] != symptoms[j][0]:
            continue
        else:
            tmp_sym_id.append(symptoms[j][2])
            tmp_sym_name.append(symptoms[j][3])
            print(symptoms[j][2], ' - ', symptoms[j][3])

    if len(tmp_sym_id) != 0:
        symptoms[i][2] = tmp_sym_id
        symptoms[i][3] = tmp_sym_name


# with open('diagnosis9.csv', mode='a', encoding='utf-8', newline='') as file:
#     file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
#     file_writer.writerow(['id_diagnosis', 'name_diagnosis', 'id_symptoms', 'name_symptoms'])
#     for sym in symptoms:
#         if type(sym[2]) == list and type(sym[3]) == list:
#             tmp_sym = [i for i in zip(sym[2], sym[3])]
#             for i in range(len(tmp_sym)):
#                 file_writer.writerow([sym[0], sym[1], tmp_sym[i][0], tmp_sym[i][1]])
#         else:
#             file_writer.writerow([sym[0], sym[1], sym[2], sym[3]])
#
#
