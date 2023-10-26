# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Create a LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.ref = self.head
            self.head = new_node

    def insert_index(self, data, index):
        new_node = Node(data)
        present_node = self.head
        position = 0
        if position == index:
            self.insert_begin(data)
        else:
            while present_node != None and position + 1 != index:
                position = position + 1
                present_node = present_node.ref

            if present_node != None:
                new_node.ref = present_node.ref
                present_node.ref = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        present_node = self.head
        while present_node.ref:
            present_node = present_node.ref

        present_node.ref = new_node

    def findNode(self, data):
        present_node = self.head
        while present_node != None and present_node.data != data:
            present_node = present_node.ref

        if present_node == None:
            return
        else:
            return present_node.data

    def remove_first_node(self):
        if self.head == None:
            return

        self.head = self.head.ref

    def remove_last_node(self):
        if self.head is None:
            return

        present_node = self.head
        while present_node.ref.ref:
            present_node = present_node.ref

        present_node.ref = None

    def remove_at_index(self, index):
        if self.head == None:
            return

        present_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while present_node != None and position + 1 != index:
                position = position + 1
                present_node = present_node.ref

            if present_node != None:
                present_node.ref = present_node.ref.ref
            else:
                print("Index not present")

    def remove_node(self, data):
        present_node = self.head

        while present_node != None and present_node.ref.data != data:
            present_node = present_node.ref

        if present_node == None:
            return
        else:
            present_node.ref = present_node.ref.ref

    def display_list(self):
        present_node = self.head
        while present_node:
            print(present_node.data)
            present_node = present_node.ref

    def reverse_list(self):
        prev = None
        present = self.head
        while present is not None:
            ref = present.ref
            present.ref = prev
            prev = present
            present = ref
        self.head = prev

    def sort_list(self):
        present_node = self.head
        while present_node != None:
            index_node = present_node.ref
            while index_node != None:
                if present_node.data > index_node.data:
                    temp = present_node.data
                    present_node.data = index_node.data
                    index_node.data = temp
                index_node = index_node.ref
            present_node = present_node.ref

# create a new linked list
linkedlist = LinkedList()

# add nodes to the linked list
linkedlist.insertAtEnd("a")
linkedlist.insertAtEnd("b")
linkedlist.insert_begin("c")
linkedlist.insertAtEnd("d")
linkedlist.insert_index("g", 2)

# print the linked list
print("Node Data")
linkedlist.display_list()

linkedlist.reverse_list()
print("\nReverse Linked List")
linkedlist.display_list()

linkedlist.sort_list()
print("\nSorted Linked List")
linkedlist.display_list()

# remove a nodes from the linked list
print("\nRemove First Node")
linkedlist.remove_first_node()
print("Remove Last Node")
linkedlist.remove_last_node()
print("Remove Node at Index 1")
linkedlist.remove_at_index(1)


# print the linked list again
print("\nLinked list after removing a node:")
linkedlist.display_list()
