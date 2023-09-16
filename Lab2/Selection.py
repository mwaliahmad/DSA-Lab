import funcs
import time as time
    
def main():
    n = 30000
    array = funcs.RandomArray(n)
    start_time = time.time()

    SelectionSort(array, 0, n) #calling selection sort algo

    end_time = time.time() 
    run_time = end_time - start_time

    print("Runtime of SelectionSort at",n,"is",run_time,"seconds")

    funcs.WriteFile("SortedSelectionSort.csv",array)  
    

def SelectionSort(array , start , end):
    for i in range(start, end, 1): 
        temp = array[i]
        idx = i
        
        for j in range(i, end, 1): # loop which find minimun in the array
            if(temp > array[j]):
                temp = array[j]
                idx = j
        
        array[idx] = array[i] # swap minimum with zero index element
        array[i] = temp

if __name__=="__main__":
    main()