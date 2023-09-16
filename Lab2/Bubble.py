import time as time
import funcs

def main():
    n = 30000
    array = funcs.RandomArray(n)

    start_time = time.time()

    BubbleSort(array, 0, n) #calling bubble sort algo

    end_time = time.time() 
    run_time = end_time - start_time

    print("Runtime of BubbleSort at",n,"is",run_time,"seconds")

    funcs.WriteFile("SortedBubbleSort.csv", array)  

def BubbleSort(array , start , end):
    a = end 
    for i in range(start, end): 
        flag = False
        for j in range(start, a-1): # loop which find minimun in the array
            
            if(array[j] > array[j+1]): # swap if next element in array is greater
                flag = True    
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        a-=1
        if not flag:
            break

if __name__=="__main__":
    main()