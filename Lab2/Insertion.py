import funcs
import time as time

def main():
    n = 30000
    array = funcs.RandomArray(n)

    start_time = time.time()

    InsertionSort(array, 0, n)  # calling insert sort algo

    end_time = time.time()
    run_time = end_time - start_time

    print("Runtime of InsertionSort at", n, "is", run_time, "seconds")

    funcs.WriteFile("SortedInsertionSort.csv", array)

def InsertionSort(array, start, end):

    for i in range(start+1,end,1):
        temp = array[i]
        j = i-1
        while(j >= 0 and array[j] > temp):
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp

if __name__=="__main__":
    main()