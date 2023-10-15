import numpy as np
import math


def main():
    print(BucketSort([0.897, 0.656, 0.565, 0.1234, 0.665, 0.3434]))


def InsertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp


def BucketSort(input):
    size = len(input)
    output = [[] for _ in range(size)]


    for i in input:
        idx = math.floor(size * i)
        bucket = output[idx]
        bucket.append(i)

    for b in output:
        InsertionSort(b)

    Result = []
    for i in range(len(output)):
        for j in range(len(output[i])):
            Result.append(output[i][j])
    return Result


if __name__ == "__main__":
    main()
