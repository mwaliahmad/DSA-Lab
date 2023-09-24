import numpy as np

def main():
    
    Input = [[1,4],[2,5],[7,9],[9,10],[6,10]]
    print(friendSlower(Input))
    print(friendsFaster(Input))
    
    
def friendSlower(Input):

    users = len(Input)
    Result = []
    for i in range(users):
        for j in range(i+1,users):
            if((Input[j][0] <= Input[i][1] <= Input[j][1]) or (Input[j][0] <=  Input[i][0] <= Input[j][1])):
                Result.append((i+1,j+1))
    return Result

def friendsFaster(Input):

    for i in range(len(Input)):
        Input[i].append(i+1)

    MergeSort(Input, 0, len(Input)-1, 0)
    First = []
    i = 0
    j = i + 1
    while(i!= len(Input)-1):
        
        if(j==len(Input)):
            i+=1
            j = i + 1        
        elif((Input[j][0] <= Input[i][1] <= Input[j][1]) or (Input[j][0] <=  Input[i][0] <= Input[j][1])):
            First.append((Input[i][2],Input[j][2]))
            j+=1
        else:
            i+=1
            j=i+1

    MergeSort(Input, 0, len(Input)-1, 1)
    Second = []
    i = 0
    j = i + 1
    while(i!= len(Input)-1):
        
        if(j==len(Input)):
            i+=1
            j = i + 1        
        elif((Input[j][0] <= Input[i][1] <= Input[j][1]) or (Input[j][0] <=  Input[i][0] <= Input[j][1])):
            Second.append((Input[i][2],Input[j][2]))
            j+=1
        else:
            i+=1
            j=i+1
    
    First = set(First)
    Second = set(Second)
    Output = First.union(Second )
    Output = list(Output)
    return Output

def MergeSort(array, start, end, index):

    mid = start + (end - start) // 2
    if(start < end):
        
        MergeSort(array, start, mid, index)
        MergeSort(array, mid + 1, end, index)

    Merge(array, start, mid, end, index)

def Merge(array, p, q, r, index):
    
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
        if(L[i][index] <= R[j][index]):
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

def Random():
    n = 4
    output = []
    for i in range(n):
        pair = []
        pair.append(np.random.randint(1,5))
        pair.append(np.random.randint(6,10))
        output.append(pair)
    return output

if __name__ == "__main__":
    main()