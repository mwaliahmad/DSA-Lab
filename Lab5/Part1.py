import time
import numpy as np


def main():
    n = 10
    array = RandomArray(n)
    start_time = time.time()

    QuickSort(array, 0, n - 1)  # calling Quick sort algo

    end_time = time.time()
    run_time = end_time - start_time

    print("Runtime of QuickSort at", n, "is", run_time, "seconds")

    WriteFile("QuickSort.csv", array)


def QuickSort(array, p, r):
    if p < r:
        q = Partition(array, p, r)
        QuickSort(array, p, q - 1)
        QuickSort(array, q + 1, r)


def Partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def RandomArray(size):
    arr = []
    for i in range(size):
        num = np.random.randint(-15000, 15000)
        arr.append(num)
    return arr


def WriteFile(filename, arr):
    f = open(file=filename, mode="w")
    for i in arr:
        f.write(str(i) + "\n")


if __name__ == "__main__":
    main()
