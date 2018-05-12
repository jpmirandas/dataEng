import string


def list_01():
    return list([char1 + char2 + str(dig1) + str(dig2) for char1 in string.ascii_lowercase for char2 in string.ascii_lowercase for dig1 in string.digits for dig2 in string.digits])


def list_02():
    # return list([x for x in range(3) for y in range(4)])
    return [[["*"]*3]*4]*6

def list_03():
    return [lambda char_1, char_2: (char_1 + char_2) (char_1, char_2) for char_1 in string.ascii_lowercase for char_2 in string.ascii_lowercase]

def list_04(dic, value):

    keys = dic.keys()
    keys = [x for x in keys if x > value]

    return [str(key) + " " + dic[key] for key in keys]

def list_05(dic1, dic2):
    items1 = dic1.items()
    items2 = dic2.items()

    return list(set(items1) & set(items2))



if __name__ == "__main__":
    # print(list_01())
    # print(list_02())
    print(list_03())
    # print (list_04({1: "asd", 2: "1da", 3: "cvxcv"}, 2))
    # print(list_05({1: "a", 2: "b", 3: "c"}, {1: "x", 2: "y", 3: "c", 4: "a"}))