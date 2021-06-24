import threading
from settings import *
from function import *
import sys

dis_sym = open_file('test.csv')
print(len(dis_sym))


# for el in dis_sym:
#     print(el)
print('#'*150)

parant_list = []
child_list = []
temp_list = []
weight = []
temp_weight = []

for el in dis_sym:
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

for el in temp_list:
    print(el)

 # child_list.append(el[1])
 #        parant_list.append(el[0])
 #        weight.append(el[2])
 #        el[0] = parant_list[child_list.index(el[0])]
 #        el[2] = weight[child_list.index(el[0])]
 #        temp_list.append(el)