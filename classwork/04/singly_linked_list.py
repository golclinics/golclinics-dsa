# the Node class - contains value and address to next node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        if idx > self.count:
            return
        if self.head == None:
            return
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def printList(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

    def sumList(self):
        tempnode = self.head
        self.sum = 0
        while (tempnode != None):
            self.sum += tempnode.get_data()
            tempnode = tempnode.get_next()
        print('Sum of list:', self.sum)



if __name__ == "__main__":
    # create a linked list and insert some items
    itemlist = LinkedList()
    itemlist.insert(3)
    itemlist.insert(10)
    itemlist.insert(1)
    itemlist.insert(5)
    itemlist.insert(6)

    #Print the List
    itemlist.printList()

    #GEt sum
    itemlist.sumList()


