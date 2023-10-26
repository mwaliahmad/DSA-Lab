from stack import Stack


def main():
    # sentence = "Hello, world!"
    # reverse_sequence(sentence)
    stack = Stack()
    while True:
        input_str = input()
        process_input(stack, input_str)


def reverse_sequence(sentence):
    stack = []

    temp = ""

    for i in range(len(sentence)):
        if sentence[i] == " ":
            stack.append(temp)
            temp = ""
        else:
            temp = temp + sentence[i]
    stack.append(temp)

    while len(stack) != 0:
        temp = stack[len(stack) - 1]
        print(temp, end=" ")
        stack.pop()


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def perform_operation(stack, operator):
    operand2 = stack.pop()
    operand1 = stack.pop()
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    elif operator == "%":
        result = operand1 % operand2
    stack.push(result)


def process_input(stack, input_str):
    if is_integer(input_str):
        stack.push(int(input_str))
    elif input_str in ["+", "-", "*", "/", "%"]:
        perform_operation(stack, input_str)
    elif input_str == "?":
        stack.print_stack()
    elif input_str == "^":
        print(stack.pop())
    elif input_str == "!":
        exit()


if __name__ == "__main__":
    main()
