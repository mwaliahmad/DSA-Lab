import numpy as np


def main():
    print(RadixSort([110, 45, 65, 50, 90, 602, 24, 2, 66]))


def RadixSort(input):
    max = input[0]
    for i in input:
        if i >= max:
            max = i

    digits = 0
    while max != 0:
        digits += 1
        max = max // 10
    output = input
    for i in range(digits):
        output = CountingSort(output, 10**i)

    return output


def CountingSort(input, place):
    output = [0] * len(input)
    max = 9
    min = 0
    diff = max - min + 1
    count = [0] * (diff)

    for i in range(len(input)):
        j = input[i] // place
        j = j % 10
        count[j - min] += 1

    for i in range(1, diff):
        count[i] += count[i - 1]

    for i in range(len(input) - 1, -1, -1):
        j = input[i] // place
        j = j % 10
        count[j - min] -= 1
        output[count[j - min]] = input[i]
    return output


if __name__ == "__main__":
    main()
