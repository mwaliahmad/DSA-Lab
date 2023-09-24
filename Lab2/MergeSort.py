import funcs
import time as time

def main():
    n = 100000
    array = funcs.RandomArray(n)

    start_time = time.time()


    MergeSort(array, 0, n-1)  # calling merge sort algo

    end_time = time.time()
    run_time = end_time - start_time

    print("Runtime of MergeSort at", n, "is", run_time, "seconds")

    funcs.WriteFile("SortedMergeSort.csv", array)

def MergeSort(array, start, end):

    mid = start + (end - start) // 2
    if(start < end):
        
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)

    funcs.Merge(array, start, mid, end)



if __name__=="__main__":
    main()