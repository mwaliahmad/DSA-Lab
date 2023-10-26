class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if not self.isFull():
            self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def isFull(self):
        return len(self.stack) == 10

    def print_stack(self):
        print(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    stack.push(6)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
