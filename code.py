from table import character_list, table


def code(word, key):
    temp = []
    tran = []
    word = word.upper()
    key = key.upper()
    if " " in key:
        print("密钥只能由字母组成！")
        exit()
    for i in range(len(word)):
        if word[i] == " ":
            temp.append(i)
    word = "".join(word.split())
    table_create = table()
    trans = ""
    for i in range(len(word)):
        if word[i] == " ":
            trans += " "
        else:
            trans += character_list[
                table_create[character_list.index(key[i % len(key)]), character_list.index(word[i])]]
    for i in range(len(trans)):
        tran.append(trans[i])
    for i in temp:
        tran.insert(i, " ")
    tran = "".join(tran)
    return tran


def decode(word, key):
    temp = []
    raw_ = []
    word = word.upper()
    key = key.upper()
    if " " in key:
        print("密钥只能由字母组成！")
        exit()
    for i in range(len(word)):
        if word[i] == " ":
            temp.append(i)
    word = "".join(word.split())
    table_create = table()
    raw = ""
    for i in range(len(word)):
        if word[i] == " ":
            raw += " "
        else:
            key1 = character_list.index(key[i % len(key)])
            for j in range(26):
                if character_list[table_create[key1, j]] == word[i]:
                    raw += character_list[j]
                    break
    for i in range(len(raw)):
        raw_.append(raw[i])
    for i in temp:
        raw_.insert(i, " ")
    raw = "".join(raw_)
    return raw
