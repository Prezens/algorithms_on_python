import random


def selection_sort(collection):
    length = len(collection)

    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k

        collection[least], collection[i] = (collection[i], collection[least])

    return collection


if __name__ == '__main__':
    unsorted = [x + random.randint(0, 500) for x in range(10)]
    print(selection_sort(unsorted))
