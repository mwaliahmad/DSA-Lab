import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # printMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (0, 0), 3, 3)

    # A = MatAdd([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # printMatrix(A, (0, 0), 3, 3)

    # B = MatAddPartial(
    #     [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], (1, 1), 2
    # )
    # printMatrix(B, (0, 0), 2, 2)

    # C = MatMul([[1, 2, 3], [4, 5, 6], [7,8,9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # printMatrix(C, (0, 0), 3, 3)

    # D = MatMulRecursive([[1, 2, 3], [4, 5, 6], [7,8,9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # printMatrix(D, (0, 0), 3, 3)
    pass


def printMatrix(A, starting_index, rows, columns):
    for i in range(starting_index[0], rows):
        for j in range(starting_index[1], columns):
            print(A[i][j], end=" ")
        print()


def MatAdd(A, B):
    rows = len(A)
    columns = len(A[0])
    C = [[0 for x in range(columns)] for y in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            C[i][j] = A[i][j] + B[i][j]
    return C


def MatAddPartial(A, B, start, size):
    rows, cols = start

    if rows < 0 or cols < 0 or rows + size > len(A) or cols + size > len(A[0]):
        return None

    A = [rows[cols : cols + size] for rows in A[rows : rows + size]]
    B = [rows[cols : cols + size] for rows in B[rows : rows + size]]
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = A[i][j] + B[i][j]

    return result


def MatMul(A, B):
    if len(A[0]) != len(B):
        return None
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def MatMulRecursive(A, B):
    if A.shape == (1, 1) and B.shape == (1, 1):
        return A[0, 0] * B[0, 0]

    if A.shape[1] != B.shape[0]:
        return None

    A_rows, A_cols = A.shape
    B_rows, B_cols = B.shape
    mid = min(A_cols, B_rows)

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    C11 = MatMulRecursive(A11, B11) + MatMulRecursive(A12, B21)
    C12 = MatMulRecursive(A11, B12) + MatMulRecursive(A12, B22)
    C21 = MatMulRecursive(A21, B11) + MatMulRecursive(A22, B21)
    C22 = MatMulRecursive(A21, B12) + MatMulRecursive(A22, B22)


    # return result


if __name__ == "__main__":
    main()
