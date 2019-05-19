import random


def comb_sort(data):
    shrink_factor = 1.247
    gap = len(data)
    swapped = True
    i = 0

    while gap > 1 or swapped:
        gap = int(float(gap) / shrink_factor)
        swapped = False
        i = 0

        while gap + i < len(data):
            if data[i] > data[i+gap]:
                data[i], data[i+gap] = data[i+gap], data[i]
                swapped = True
            i += 1

    return data


if __name__ == '__main__':
    unsorted = [x + random.randint(0, 500) for x in range(10)]
    print(comb_sort(unsorted))
