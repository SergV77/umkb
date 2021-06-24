def makeGroupSymptoms(item, base):
    group_sym = [makeGroupSymptoms(sym[9], base) for sym in base if item == sym[7]]
    if len(group_sym) > 0:
        return group_sym
    else:
        return item


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
def prepareGroup(base):
    big_block = {}
    for el in base:
        block_idb = []
        while el[3] == '0':
            for sym in base:
                while sym[3] == '1':
                    if el[0] == sym[7]:
                        block_idb.append(sym[9])
                if len(block_idb) > 0:
                    big_block[el[0]] = block_idb

    return big_block

def get_block(symtoms):
    big_block = {}
    temp_dict = list({sym[7] for sym in symtoms})

    for el in temp_dict:
        block = []
        for sym in symtoms:
            print('1 - ', el)
            print('2 - ', sym)
            print('4 - ', int(sym[7]))
            if el == int(sym[7]):
                print('3 - ', sym)
                block.append((el[9], el[11]))
                print(block)
        if len(block) > 0:
            print('4 - ', block)
            big_block[el] = block
            print('5 - ', big_block)

    return big_block
