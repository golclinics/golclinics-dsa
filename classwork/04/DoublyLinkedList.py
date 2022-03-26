import functools


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
        
# This decorator states that the element can't run if empty
def is_empty(func):
    @functools.wraps(func)
    def wrapper(self, *args):
        if not self.is_empty():
            return func(self, *args)
        print("You cannot do the operation when the DS is empty")
        return
    return wrapper


# Possible add functionality ?
def increase_count(func):
    @functools.wraps(func)
    def wrapper(self, *args):
        value = func(self, *args)
        self.count += 1
        return value
    return wrapper


def decrease_count(func):
    @functools.wraps(func)
    def wrapper(self, *args):
        value = func(self, *args)
        self.count -= 1
        return value
    return wrapper


def check_index(func):
    @functools.wraps(func)
    def wrapper(self, index, *args):
        if index < 0 or index >= self.size():
            raise IndexError("The index being used is NA")
            return
        else:
            return func(self, index, *args)
    return wrapper
            
     
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    @increase_count
    def push(self, data):
        current_node = Node(data)
        if self.is_empty():
            self.head = current_node
        else:
            if self.tail is None:
                self.tail = current_node
                self.head.next = self.tail
                self.tail.previous = self.head
            else:
                self.tail.next = current_node
                current_node.previous = self.tail
                self.tail = current_node

    @increase_count
    def push_left(self, data):
        current_node = Node(data)
        if self.is_empty():
            self.head = current_node
        elif self.size() == 1:
            self.head.previous = current_node
            current_node.next = self.head
            self.head = current_node
            self.tail = current_node.next
        else:
            self.head.previous = current_node
            current_node.next = self.head
            self.head = current_node

    @decrease_count
    @check_index
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == self.size() - 1:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            current_node = self.find_node(index, True)
            previous_node = current_node.previous
            next_node = current_node.next
            previous_node.next = next_node

    @is_empty
    @decrease_count
    def pop(self):
        if self.size() == 1:
            current_data = self.head.data
            self.head = None
        elif self.size() == 2:
            current_data = self.tail.data
            self.tail = None
        else:
            current_data = self.tail.data
            self.tail = self.tail.previous
            self.tail.next = None
        return current_data 

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    @check_index
    def insert(self, index, data):
        # I will not be adding the @increase_count decoration due to this
        if index == 0:
            self.push_left(data)
        else:
            next_node = self.find_node(index, True)
            previous_node = next_node.previous
            current_node = Node(data)
            previous_node.next = current_node
            current_node.next = next_node
            next_node.previous = current_node
            current_node.previous = previous_node
            self.count += 1

    @check_index
    def find_node(self, index, node = False):
        current_node = self.head
        i = 0
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node if node else current_node

    def print_list(self):
        current_node = self.head
        i = 0
        while current_node is not None:
            if i == self.size() - 1:
                print(current_node.data)
            else:
                print(current_node.data, ' -- ', end = '')
            current_node = current_node.next
            i += 1


if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.push(3)
    linked_list.push(10)
    linked_list.push(5)
    linked_list.push(1)
    linked_list.push(6)

    print("Printing the entire initiated list")
    linked_list.print_list()
    print("Inserting the data 25 at index 2 then printing")
    linked_list.insert(2, 25)
    linked_list.print_list()
    print("Inserting 1 at the index 0 then printing")
    linked_list.push_left(1)
    linked_list.print_list()
    print(linked_list.size())
    print("Popping then printing")
    print(linked_list.pop())
    linked_list.print_list()
