class Node:
    def __init__(self, data):
        self._data = data
        self.next = None
        # self.prev = None

    


class Linkedlist:

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    # Done
    def push(self, data):
        if self.isEmpty():
            self._head = Node(data)
        else:
            if self._tail is None:
                self._tail = Node(data)
                self._head.next = self._tail
            else:
                self._tail.next = Node(data)
                self._tail = self._tail.next
        self._count += 1

    # Done
    def remove(self, index):
        if index < 0 or index >= self.size():
            raise IndexError
            return
        if index == 0:
            # Removing from the head
            self._head = self._head.next
            self._count -= 1
            return
        previous_node = self.findNode(index - 1, True)
        if index == self.size() - 1:
            # Removing from the last index
            self._tail = previous_node
        else:
            # Removing from the middle
            previous_node.next = previous_node.next.next
        self._count -= 1

    # Done
    def pop(self):
        if self.isEmpty():
            # Popping an empty list
            return
        if self.size() == 1:
            # Popping a list with size = 1, From the head
            current_data = self._head.data
            self._head = None
        elif self.size() == 2:
            # Popping a list with size = 2, From the tail
            current_data = self._tail.data
            self._tail = None
        else:
            # Popping a list with size > 2
            previous_node = self.findNode(self.size() - 2, True)
            current_data = self._tail.data
            self._tail = previous_node
            self._tail.next = None
        self._count -= 1
        return current_data
        
    # Done
    def size(self):
        return self._count

    # Done
    def isEmpty(self):
        return self.size() == 0

    # Done
    def insert(self, index, data):
        if index == 0:
            # Inserting at the head
            current_node = Node(data)
            current_node.next = self._head
            self._head = current_node
            self._count += 1
            return
        # Find the node before the index    
        previous_node = self.findNode(index - 1, True)
        # Find the node at the index
        next_node = previous_node.next
        current_node = Node(data)
        # Set the node at the index
        previous_node.next = current_node
        # Push the previous next node
        current_node.next = next_node
        self._count += 1

    # Done
    def findNode(self, index, node = False):
        current_node = self._head
        if index >= self.size() or index < 0:
            raise IndexError
            return
        i = 0
        while i < index:
            current_node = current_node.next
            i += 1
        return current_node if node else current_node

    def printList(self):
        current_node = self._head
        i = 0
        while current_node is not None:
            if i == self.size() - 1:
                # To avoid the last ->
                print(current_node._data)
            else:
                print(current_node._data , end = ' -> ')
            current_node = current_node.next
            i += 1

    def sum(self):
        current_node = self._head
        total = 0
        while current_node is not None:
            total += current_node._data
            current_node = current_node.next
        return total

linked_list = Linkedlist()
linked_list.push(3)
linked_list.push(10)
linked_list.push(5)
linked_list.push(1)
linked_list.push(6)
print("Printing the entire initiated list")
linked_list.printList()
print("The sum is =", linked_list.sum())
print("Inserting the data 25 at index 2 then printing")
linked_list.insert(2, 25)
linked_list.printList()
print("The sum is =", linked_list.sum())
print("Removing the data at index 2 then printing")
linked_list.remove(2)
linked_list.printList()
print("The sum is =", linked_list.sum())

