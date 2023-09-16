import funcs
import time as time
import Selection as S
import Insertion as I
import Bubble as B
import MergeSort as M
import HybridMerge as HM


def main():
    
    n = funcs.ReadFile("Nvalues.txt")
    Table = []
    for i in n:
        line = []
        line.append(i)
        
        
        array = funcs.RandomArray(i)
        start_time = time.time()
        I.InsertionSort(array, 0, i)  # calling insertion sort algo
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        array = funcs.RandomArray(i)
        start_time = time.time()
        M.MergeSort(array, 0, i-1)  # calling merge sort algo
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        array = funcs.RandomArray(i)        
        start_time = time.time()
        HM.HybridMergeSort(array, 0, i-1)  # calling hybrid merge sort algo
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)

        array = funcs.RandomArray(i)        
        start_time = time.time()
        S.SelectionSort(array, 0, i)  # calling selection sort algo
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        array = funcs.RandomArray(i)        
        start_time = time.time()
        B.BubbleSort(array, 0, i)  # calling bubble sort algo
        end_time = time.time()
        run_time = end_time - start_time
        line.append(run_time)
        
        Table.append(line)
    
    funcs.WriteTable("RunTime.csv", Table)
    


if __name__=="__main__":
    main()