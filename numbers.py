import numpy as np


def ex_01(list):
    return np.array(list)


def ex_02():
    output = np.random.randint(4, size=(5, 5))

    with open('output_numpy.txt', 'w') as file:
        file.write(str(output))


def ex_03():
    numbers = np.array(range(100))
    numbers = np.array(filter(lambda x: x % 3 == 0 | x % 5 == 0, numbers))
    return np.sum(numbers)


def ex_04(list):
    return np.unique(list)


def ex_05(list1, list2):
    return np.intersect1d(list1, list2)



if __name__ == "__main__":
    print("Tuple: "),
    print(ex_01((1, 2)))
    print("List: "),
    print(ex_01(range(4)))
    print(ex_02())
    print(ex_03())
    print(ex_04([1, 2, 6, 2, 7]))
    print(ex_05([1, 2, 6, 2, 7], [7]))

