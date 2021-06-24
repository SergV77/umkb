import threading
from settings import *
from function import *
import sys


dis_sym = open_file('test.csv')
print(len(dis_sym))

#Группировка симптомов по глубине
deep = {int(sym[3]) for sym in dis_sym_all[count_diag+1:]}


# for el in dis_sym:
#     print(el)
print('#'*150)
# diag = {sym1[0] for sym1 in dis_sym}
# deep = {int(line[3]) for line in dis_sym}


# def make_recurs_list(temp_list, base):
#     big_temp = []
#     for el in temp_list:
#         temp = []
#         for sym in base:
#             if el[0] == sym[0]:
#                     temp.append((sym[1], sym[2], sym[3]))
#
#         if len(temp) > 0:
#             big_temp.append(make_recurs_list(temp, base))
#
#         big_temp.append(el)
#
#     return big_temp


new_dis_sym = []
for el1 in dis_sym:
    if el1[3] == '1':
        temp_list = []
        #temp_list2 = []
        for el2 in dis_sym:
            if el1[1] == el2[0]:
                temp_list.append((el2[1], el2[2], el2[3]))

        if len(temp_list) > 0:
            #temp_list2 += [(el1[1], el1[2], el1[3])]
            #temp_list2 += temp_list
            el1[1] = temp_list

        new_dis_sym.append(el1)


def make_recurs_list(item_list, base):
    item_list = extract_list(item_list)
    for el in item_list:
        temp_list = []
        #temp_list2 = []
        for sym in base:
            if el[0] == sym[0]:
                temp_list.append((sym[1], sym[2], sym[3]))

        if len(temp_list) > 0:
            #temp_list2 += [el]
            #temp_list2 += temp_list
            item_list[item_list.index(el)] = temp_list



    return item_list



for i in range(3):
    for el in new_dis_sym:
        if type(el[1]) == list:
            el[1] = make_recurs_list(el[1], dis_sym)
    print(i)

for el in new_dis_sym:
    print(el)


#
#
# def make_recurs_list(temp_list, base):
#     big_temp = []
#     for el in temp_list:
#         temp = []
#         for sym in base:
#             if el[0] == sym[0]:
#                 temp.append((sym[1], sym[2], sym[3]))
#
#         if len(temp) > 0:
#             big_temp.append(make_recurs_list(temp, base))
#
#         big_temp.append(el)
#
#     return big_temp
#
#
# new_dis_sym = []
# for el1 in dis_sym:
#     if el1[3] == '1':
#         temp_list = []
#         for el2 in dis_sym:
#             if el1[1] == el2[0]:
#                 temp_list.append((el2[1], el2[2], el2[3]))
#
#         if len(temp_list) > 0:
#             el1[1] = make_recurs_list(temp_list, dis_sym)
#
#         new_dis_sym.append(el1)








 # def make_recurs(item, base):
#     temp2 = []
#     if len(temp) > 0:
#         for el in temp:
#             temp2.append(make_recurs_list((sym[1], sym[2], sym[3]), base))
#         return temp2


#
# def make_recurs_list(atom, base):
#     #temp = []
#     for sym in base:
#         if atom[0] == sym[0]:
#             return make_recurs_list((sym[1], sym[2], sym[3]), base)
#
#     return atom
#
#
# new_dis_sym = []
# for el1 in dis_sym:
#     temp_list = []
#     for el2 in dis_sym:
#         if el1[1] == el2[0]:
#             temp_list.append(make_recurs_list((el2[1], el2[2], el2[3]), dis_sym))
#
#     if len(temp_list) > 0:
#         el1[1] = temp_list

# new_dis_sym = []
# for el1 in dis_sym:
#     temp_list = []
#     for el2 in dis_sym:
#         if el1[1] == el2[0]:
#             temp_list.append(make_recurs_list((el2[1], el2[2], el2[3]), dis_sym))
#         else:
#             new_dis_sym.append(el1)
#     if len(temp_list) > 0:
#         el1[1] = temp_list

#
# new_big_list = []
# for i in range(len(deep)):
#     new_list = []
#     for line in dis_sym:
#         if line[3] == str(i+1):
#             new_list.append(line)
#     new_big_list.append(new_list)

# for el in new_big_list:
#     print(el)
#
# def make_list(el_list, base):
#     temp_list = []
#     for sym in base:
#         if el_list == sym[0]:
#             temp_list.append(make_list(sym[1], base))
#         else:
#             temp_list.append(el_list)
#
#
#         if len(temp_list) > 0:
#             el_list = temp_list
#     return el_list
#
#
#
# for el in new_big_list[0]:
#     temp_list = []
#     for sym in new_big_list[1]:
#         if el[1] == sym[0]:
#             temp_list.append(make_list(sym[1], new_big_list[2:]))
#
#     if len(temp_list) > 0:
#         el[1] = temp_list



# for el in new_big_list[0]:
#     if type(el[1]) == list:
#         el[1] = make_list(el[1], new_big_list[2])


# for el in new_big_list[0]:
#     temp_list = []
#     for sym in new_big_list[1]:
#         if el[1] == sym[0]:
#             temp_list.append(sym)
#
#     if len(temp_list) > 0:
#         el[1] = temp_list
#
#
#
# for el in new_big_list[0]:
#     if type(el[1]) == list:
#         el[1] = make_list(el[1], new_big_list[2])


# i = 1
# for el in new_big_list[0]:
#     temp_list = []
#     el[1] = make_list(el, new_big_list[i+1])
#     i += 1

# def make_list(el_list, base):
#     for el in el_list:
#         temp_list = []
#         for sym in base:
#             if el[1] == sym[0]:
#                 temp_list.append(make_list(sym, base))
#
#         if len(temp_list) > 0:
#             el[1] = temp_list
#     return el_list

# print(len(deep))
# print(len(new_big_list))
# for el in new_big_list[0]:
#     print(el)
#

#
# for el in new_big_list[0]:
#     temp_list = []
#     for sym in new_big_list[1]:
#         if el[1] == sym[0]:
#             temp_list.append(sym)
#
#     if len(temp_list) > 0:
#         el[1] = temp_list


#
# for el in new_big_list[0]:
#     temp_list = []
#
#     for sym in new_big_list[1]:
#         if el[1] == sym[0]:
#             temp_list.append(sym)
#
#     if len(temp_list) > 0:
#         el[1] = temp_list
#



# new_list = []
# all_id = []
# for sym1 in dis_sym:
#     sym_id = []
#     for sym2 in dis_sym:
#         if sym1[1] == sym2[0]:
#             sym_id.append(sym2[1])
#
#     if len(sym_id) != 0:
#         sym1[1] = extract_list(sym_id)
#
#
# for el in dis_sym:
#     if el[3] == 1:
#         print(el)



# diag = {sym1[0] for sym1 in dis_sym}
# print(len(diag))
#
#
# new_list = []
# all_id = []
# for el in diag:
#     sym_id = []
#     for sym in dis_sym:
#         if sym1[1] == sym2[0]:
#             sym_id.append(sym2[1])
#
#     if len(sym_id) != 0:
#         sym1[1] = extract_list(sym_id)

#
# new_lib = {}
# all_id = []
# for el in diag:
#     sym_id = []
#     for sym in dis_sym:
#         if el == sym[0]:
#             sym_id.append((sym[1], sym[2]))
#
#     if len(sym_id) != 0:
#         new_lib[el] = sym_id


#
#
# for k, v in new_lib.items():
#     print(k, ' - ', v)

# def make_recurs_list(atom, base):
#     temp = []
#     for sym in base:
#         if atom[0] == sym[0]:
#             temp.append(make_recurs_list((sym[1], sym[2], sym[3]), base))
#             if len(temp) > 0:
#                 return temp
#         else:
#             temp = [atom]
#     return temp
#
#
# new_dis_sym = []
# for el1 in dis_sym:
#     if el1[3] == '1':
#         temp_list = []
#         for el2 in dis_sym:
#             if el1[1] == el2[0]:
#                 temp_list.append(make_recurs_list((el2[1], el2[2], el2[3]), dis_sym))
#
#         if len(temp_list) > 0:
#             el1[1] = temp_list
#
#         new_dis_sym.append(el1)
#
#
#
# for el in new_dis_sym:
#     print(el)

# diag = {sym1[0] for sym1 in dis_sym}
#
# big_temp = {}
# for el in diag:
#     temp = []
#     for el2 in dis_sym:
#         if el == el2[0]:
#             temp.append((el2[1], el2[2], el2[3]))
#     big_temp[el] = temp
#
# for k, v in big_temp.items():
#     print(k, ' - ', v)
# print('#'*150)
# for k, v in big_temp.items():
#     for el1 in v:
#         for el2 in diag:
#             if el1[0] == el2:
#                 v[v.index(el1)] = (big_temp[el2], el1[1], el1[2])
#
# for k, v in big_temp.items():
#     print(k, ' - ', v)
#
# def make_recurs_list(temp_list, base):
#     big_temp = []
#     for el in temp_list:
#         temp = []
#         for sym in base:
#             if el[0] == sym[0]:
#                     temp.append((sym[1], sym[2], sym[3]))
#
#         if len(temp) > 0:
#             big_temp.append(make_recurs_list(temp, base))
#
#         big_temp.append(el)
#
#     return big_temp
#
#
# new_dis_sym = []
# for i in range(len(dis_sym)):
#     for el1 in dis_sym:
#         if el1[3] == '1':
#             temp_list = []
#             for el2 in dis_sym:
#                 if el1[1] == el2[0]:
#                     temp_list.append((el2[1], el2[2], el2[3]))
#
#         if len(temp_list) > 0:
#             el1[1] = make_recurs_list(temp_list, dis_sym)
#
#         new_dis_sym.append(el1)
#
#
# for el in new_dis_sym:
#     print(el)


