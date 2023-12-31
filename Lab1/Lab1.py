# helping functions

def ReadFile(path):
    file = open(file=path ,mode='r')
    lines = file.read()
    numbers = []
    arr = lines.split()
    for i in arr:
        num = int(i)
        numbers.append(num)
        
    return numbers

# Problem 1
def SearchA(Arr, x):
    result = []
    for i in range(len(Arr)):
        if(x==Arr[i]):
            result.append(i)
    return result
        

Numbers = ReadFile("problem1.txt")
print(SearchA(Numbers, 2))            
            
# Problem 2

# In a O(n) and in o(1)

# Problem 3
def Minimun(Arr, Starting, Ending):
    
    result = min(Arr[Starting:Ending+1])
            
    return result

Numbers = ReadFile("problem3.txt")
print(Minimun( Numbers, 4, 7))
            
# Problem 4

def Sort4(Arr):
    Sorted = []
    while (len(Arr)!=0):
        result = Minimun(Arr, 0, len(Arr))
        Arr.remove(result)
        Sorted.append(result)
       
    return Sorted


Numbers = ReadFile("problem3.txt")
print (Sort4(Numbers))

# Problem 5

def StringReverse(Str, Starting, Ending):
    
    Result1 = Str[Starting:Ending+1]
    Result = Result1[::-1]
    return Result
     
print(StringReverse("University of Engineering and Technology Lahore", 27, 38))

# Problem 6

def SumIterative(number):
    sum = 0
    while(number != 0):
        sum = sum + (number%10)
        number = number//10
    
    return sum

def SumRecursive(number):
    
    if number == 0:
        return number
    else:
        return number%10 + SumRecursive(number//10)

print(SumIterative(1524))
print(SumRecursive(1524))

# Problem 7

def ColumnWiseSum(Mat):
    Sum = []
    colSum = 0
    for i in range(len(Mat[0])):
        for j in range(len(Mat[1])):
            colSum = colSum + Mat[i][j]
        Sum.append(colSum)
        colSum = 0
        
    return Sum
def RowWiseSum(Mat):
    Sum = []
    rowSum = 0
    for i in range(len(Mat[1])):
        for j in range(len(Mat[0])):
            rowSum = rowSum + Mat[j][i]
        Sum.append(rowSum)
        rowSum = 0
        
    return Sum
            
print(ColumnWiseSum([[1, 5, 4], [13, 11, 4],[ 13, 6, 9]]))  
print(RowWiseSum([[1, 5, 4], [13, 11, 4],[ 13, 6, 9]]))    
    
# Problem 8

def SortedMerge(Arr1, Arr2):
    
    Arr = Arr1 + Arr2
    return Sort4(Arr) 


Numbers1 = ReadFile("problem8.1.txt")
Numbers2 = ReadFile("problem8.2.txt")
print(SortedMerge(Numbers1, Numbers2)) 

# Problem 9

def RecursiveFunction(Str, left, right):
    if left>=right:
        return True
    if Str[left] != Str[right]:
        return False
    return RecursiveFunction(Str, left+1, right-1)

def PalindromRecursive(Str):
    left = 0
    right = len(Str) - 1
    
    flag = RecursiveFunction(Str, left, right)
    if(flag):
        return "Palindrom"
    else:
        return "Not Palindrom"
    
print(PalindromRecursive("radar"))

# Problem 10

def Sort10(Arr):
    Arr = Sort4(Arr)
    pos = [i for i in Arr if i>=0]
    neg = [i for i in Arr if i<0]
    ArrFinal = []
    while (pos and neg):
        ArrFinal.append(neg.pop(0))
        ArrFinal.append(pos.pop(0))
    ArrFinal.extend(pos)
    ArrFinal.extend(neg)
    
    return ArrFinal
    

Numbers = ReadFile("problem10.txt")
print(Sort10(Numbers))
        










  