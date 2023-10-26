class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isFull(self):
        return len(self.items) == 10


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.size())
print(queue.dequeue())
print(queue.size())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.size())
print(queue.dequeue())
print(queue.is_empty())
