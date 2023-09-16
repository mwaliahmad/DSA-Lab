import funcs
import time as time
import Insertion  as I
import MergeSort as M

def main():
    
    words = funcs.ReadWords("words.txt")
    before = []
    start_time = time.time()
    I.InsertionSort(words, 0, len(words))  # calling insertion sort algo
    end_time = time.time()
    run_time = end_time - start_time
    before.append(run_time)
    
    start_time = time.time()
    M.MergeSort(words, 0, len(words)-1)  # calling merge sort algo
    end_time = time.time()
    run_time = end_time - start_time
    before.append(run_time)
    
    funcs.ShuffleArray(words, 0, len(words)-1) # shuffle array
    
    after = []
    start_time = time.time()
    I.InsertionSort(words, 0, len(words))  # calling insertion sort algo
    end_time = time.time()
    run_time = end_time - start_time
    after.append(run_time)
    
    start_time = time.time()
    M.MergeSort(words, 0, len(words)-1)  # calling merge sort algo
    end_time = time.time()
    run_time = end_time - start_time
    after.append(run_time)
    
    print("Before Shuffle(InsertionSort, MergeSort):" , before)
    print("After Shuffle(InsertionSort, MergeSort):" , after)

if __name__ =="__main__":
    main()