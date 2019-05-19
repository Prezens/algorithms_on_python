import random


def insertion_sort(A):
    for i in range(1, len(A)):
        while i > 0 and A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1

    return A


if __name__ == '__main__':
    array = [x + random.randint(0, 500) for x in range(10)]
    print(insertion_sort(array))
