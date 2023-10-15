import numpy as np


def main():
    print(CountingSort([-5, -10, 0, -3, 8, 5,-1, 10]))


def CountingSort(input):
    max = input[0]
    output = [0] * len(input)

    for i in input:
        if i >= max:
            max = i
    min = input[0]
    output = [0] * len(input)
    for i in input:
        if i <= min:
            min = i
    diff = max - min +1

    count = [0] * (diff)

    for i in range(len(input)):
        j = input[i]
        count[j-min] += 1

    for i in range(1, diff):
        count[i] += count[i - 1]

    for i in range(len(input) - 1, -1, -1):
        j = input[i]
        count[j-min] -= 1
        output[count[j-min]] = input[i]
    return output


if __name__ == "__main__":
    main()
