def main():
    
    print(Multiply_integer(5645,2455))
    print(Multiply_string("5645","2455"))
    Visualize_Karatsuba("5645","2455")
    print(Multiply_Recursive("5645","2455"))
    print(Karatsuba_Recursive("5645","2455"))
    print(Multiply2("1001010110", "1110011001"))
    print(Multiply16("A85B", "D63E"))

def Multiply_integer(a, b):
    
    carry = 0
    all_Steps = []
    step = 0
    
    while(b != 0):
        partial = [0] * step 
        carry = 0
        num = a
        while(num != 0):
            multiply = (b % 10) * (num % 10)
            partial.append(carry + (multiply % 10))
            carry = multiply // 10
            num = num // 10
        if(carry != 0):
            partial.append(carry)
        step+=1
        all_Steps.append(partial)
        b = b // 10
    
    AddZeros(all_Steps)
    Sum = AddSteps(all_Steps)
    Sum = Sum[::-1]
    return "".join(map(str,Sum))

def Multiply_string(a, b):
    carry = 0
    all_steps = []
    step = 0
    length = len(b)-1
    while length >=0 :
        partial = [0] * step
        carry = 0
        b_digit = int(b[-1])
        
        for digit in a[::-1]:
            multiply = int(digit) * b_digit
            partial.append(carry + (multiply % 10))
            carry = multiply // 10
        
        if carry != 0:
            partial.append(carry)
        
        step += 1
        all_steps.append(partial)
        b = b[:-1]
        length-=1
    
    add_zeros(all_steps)
    
    result_sum = add_steps(all_steps)
    
    return "".join(map(str, result_sum[::-1]))

def Visualize_Karatsuba(a, b):
    second = b
    carry = 0
    all_steps = []
    step = 0
    length = len(b)-1
    while length >=0 :
        partial = [0] * step
        carry = 0
        b_digit = int(second[-1])
        
        for digit in a[::-1]:
            multiply = int(digit) * b_digit
            partial.append(carry + (multiply % 10))
            carry = multiply // 10
        
        if carry != 0:
            partial.append(carry)
        
        step += 1
        all_steps.append(partial)
        second = second[:-1]
        length-=1
    add_zeros(all_steps)
    print(a)
    print(b)
    print("--------")

    for step in all_steps:
        Output = "".join(map(str, step[::-1]))
        print(Output)
    
    print("--------")
    result_sum = add_steps(all_steps)
    Result = "".join(map(str, result_sum[::-1]))
    print(Result)

def Multiply_Recursive(a, b):
    if len(b) == 1:
        return SingleRecursion(a, b)
    else:
        Multiproduct = Multiply_Recursive(str(int(a)*10), b[:-1])
        Singleproduct = SingleRecursion(a, b[-1])

        return str(int(Multiproduct)+int(Singleproduct))

def Karatsuba_Recursive(a, b):
    x,y = a,b
    if not x or not y:
        return '0'

    n = max(len(x), len(y))

    if n == 1:
        return str(int(x) * int(y))

    else:
        half = (n + 1) // 2
        a = x[:-half]
        b = x[-half:]
        c = y[:-half]
        d = y[-half:]

        ac = int(Karatsuba_Recursive(a, c))
        ad = int(Karatsuba_Recursive(a, d))
        bc = int(Karatsuba_Recursive(b, c))
        bd = int(Karatsuba_Recursive(b, d))

        return str(((ac) * (10 ** n)) + ((ad + bc) * (10 ** half)) + bd)

def Multiply2(x,y):
    if not x or not y:
        return '0'

    n = max(len(x), len(y))

    if n == 1:
        return str(int(x, 2) * int(y, 2))

    else:
        half = (n + 1) // 2
        a = x[:-half]
        b = x[-half:]
        c = y[:-half]
        d = y[-half:]

        ac = int(Multiply2(a, c), 2)
        ad = int(Multiply2(a, d), 2)
        bc = int(Multiply2(b, c), 2)
        bd = int(Multiply2(b, d), 2)

        return format(((ac) * (2 ** n)) + ((ad + bc) * (2 ** half)) + bd, 'b')

def Multiply16(x, y):
    if not x or not y:
        return '0'

    n = max(len(x), len(y))

    if n == 1:
        return hex(int(x, 16) * int(y, 16))

    else:
        half = (n + 1) // 2
        a = x[:-half]
        b = x[-half:]
        c = y[:-half]
        d = y[-half:]

        ac = int(Multiply16(a, c), 16)
        ad = int(Multiply16(a, d), 16)
        bc = int(Multiply16(b, c), 16)
        bd = int(Multiply16(b, d), 16)

        result = (ac << (4 * half)) + ((ad + bc) << (4 * (half // 2))) + bd
        return hex(result)[2:]

def SingleRecursion(a, b):
    if (len(a) == 1):
        return str(int(a) * int(b))

    else:
        digit = SingleRecursion(a[1:], b)
        a = a[0] + "0" * (len(a) - 1)
        return str((int(a) * int(b)) + int(digit))

def add_zeros(steps):
    max_len = max(len(step) for step in steps)
    for step in steps:
        while len(step) < max_len:
            step.append(0)

def add_steps(steps):
    Output = []
    sum = 0
    carry = 0
    for i in range(len(steps[0])):
        for j in range(len(steps)):
            sum+=int(steps[j][i])
        sum+=carry
        Output.append(sum % 10)
        carry = sum // 10
        sum = 0
    return Output

def AddZeros(Steps):
    length = max(len(step) for step in Steps)
    for step in Steps:
        while len(step) < length:
            step.append(0)

def AddSteps(Steps):
    Output = []
    sum = 0
    carry = 0
    for i in range(len(Steps[0])):
        for j in range(len(Steps)):
            sum+=Steps[j][i]
        sum+=carry
        Output.append(sum % 10)
        carry = sum // 10
        sum = 0
    return Output

if __name__ == "__main__":
    main()