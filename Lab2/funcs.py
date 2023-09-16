import csv
import numpy as np
import time

#Example 1
def main():
    start_time = time.time()
    n = 1500
    # ans= factorial(n)
    end_time = time.time()
    runtime = end_time - start_time
    # print("Runtime of factorial at",n,"is",runtime,"seconds")

def factorial(n):
    if(n==0):
        return 1
    else:
        return n* factorial(n-1)

def RandomArray(size):
    arr = []
    for i in range(size):
        num = np.random.randint(-15000,15000)
        arr.append(num)
    return arr

def ReadFile(filename):
    f = open(file = filename , mode = 'r')
    lines = f.read()
    numbers = []
    arr = lines.split()
    for s in arr:
        num = int(s)
        numbers.append(num)
    return numbers

def ReadWords(filename):
    f = open(file = filename , mode = 'r')
    lines = f.read()
    words = []
    arr = lines.split()
    for s in arr:
        words.append(s)
    return words

def WriteFile(filename, arr):
    f = open(file = filename , mode = 'w')
    for i in arr:
        f.write(str(i) + "\n")

def WriteTable(filename, array):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in array:
            writer.writerow(row)

def Merge(array, p, q, r):
    
    len_Left = q - p + 1 # set length
    len_Right = r - q
    
    L = [0] * len_Left   # copy arrays into two parts
    R = [0] * len_Right
    
    for i in range(0, len_Left):
        L[i] = array[p + i]

    for j in range(0, len_Right):
        R[j] = array[q + 1 + j]
    
    i = 0
    j = 0
    k = p
    
    while(i < len_Left  and j < len_Right):
        if(L[i] <= R[j]):
            array[k] = L[i]
            i+=1
        else:
            array[k] = R[j]
            j+=1
        k+=1
    
    while(i<len_Left):
        array[k] = L[i]
        i+=1
        k+=1

    while(j<len_Right):
        array[k] = R[j]
        j+=1
        k+=1

def ShuffleArray(array, start, end):

    for i in range(end, start, -1):
        j = np.random.randint(start, i)
        array[i], array[j] = array[j], array[i]

if __name__=="__main__":
    main()