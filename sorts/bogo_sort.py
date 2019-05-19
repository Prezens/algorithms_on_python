import random


def isSorted(collection):
    if len(collection) < 2:
        return True
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            return False
    return True


def bogosort(collection):
    while not isSorted(collection):
        random.shuffle(collection)
    return collection


if __name__ == '__main__':
    unsorted = list(map(int, input('Введите числа через пробел > ').split()))
    print(bogosort(unsorted))
