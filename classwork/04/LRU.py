from DoublyLinkedList import DoublyLinkedList as LinkedList


class LRU(LinkedList):
    def __init__(self, max_length = 5):
        super().__init__()
        self.max_length = max_length
        self.hash_set = set()

    def push(self, data):
        if self.size() < self.max_length:
            super().push_left(data)
            self.hash_set.add(data)
        else:
            # We remove the last element
            last_data = self.pop()
            self.hash_set.remove(last_data)
            self.push(data)

    def get(self, data):
        if data in self.hash_set:
            # We find it then take it to the start
            # Also return the data
            current_node = self.head
            i = 0
            while current_node.data != data:
                current_node = current_node.next
                i += 1
            # This will remove the data from the list
            self.remove(i)
            # This will push the data to the start of the list
            self.push(data)
            
        else:
            print("Page Exception: Page not found. Adding to start")
            self.push(data)

if __name__ == '__main__':
    short_LRU = LRU(5)
    short_LRU.push(3)
    short_LRU.push(10)
    short_LRU.push(5)
    short_LRU.push(1)
    short_LRU.push(6)
    print("Printing the entire initiated list")
    short_LRU.print_list()
    print(short_LRU.count)
    print(short_LRU.max_length)
    print("Adding a new page into the list then printing")
    short_LRU.push(25)
    short_LRU.print_list()
    print(short_LRU.count)
    print(short_LRU.max_length)
    print("Searching for the removed 3 then adding it to the front of the list")
    short_LRU.get(3)
    short_LRU.print_list()
    print("Searching for 1 then adding it to the front of the list")
    short_LRU.get(1)
    short_LRU.print_list()
