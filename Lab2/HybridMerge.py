import funcs
from Insertion import InsertionSort
import time as time

def main():
    n = 100000
    array = funcs.RandomArray(n)

    start_time = time.time()


    HybridMergeSort(array, 0, n-1)  # calling hybrid merge sort algo

    end_time = time.time()
    run_time = end_time - start_time

    print("Runtime of HybridMergeSort at", n, "is", run_time, "seconds")

    funcs.WriteFile("SortedHybridSort.csv", array)

def HybridMergeSort(array, start, end):

    if ((end - start) > 16):
	
        mid = (start + end) // 2
        HybridMergeSort(array, start, mid)
        HybridMergeSort(array, mid + 1, end)
        funcs.Merge(array, start, mid, end)
    
    InsertionSort(array, start+1, end+1)

if __name__=="__main__":
    main()