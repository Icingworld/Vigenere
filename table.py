import numpy as np

table_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']


def move(_list_, num):
    list_ = []
    for i in range(26):
        list_.append(_list_[i])
    for i in range(num):
        list_.insert(len(list_), list_[0])
        list_.remove(list_[0])
    return list_


def table():
    zero = np.ones((26, 26), dtype=np.uint8)
    for i in range(26):
        tb_list = move(table_list, i)
        for j in range(26):
            zero[i, j] = tb_list[j]
    return zero
