class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_item = self.head.data
        self.head = self.head.next
        self._size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

