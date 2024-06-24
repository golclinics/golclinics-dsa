# class for each node of the linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    # only inforamation you need to store is where the list starts
    def __init__(self):
        self.head = None

    def __repr__(self):

        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        
        return "->".join(nodes)

    def printList(self):
        print(self)

    def reverse(self, llist):
        if not llist.head or not llist.head.next:
            return llist.head
        # initialize variables
        previous = None
        current = llist.head
        following = current.next

        while current is not None:
            current.next = previous # reverse the link
            previous = current # move previous one step ahead
            current = following # move current one step ahead

            if following is not None: # if current wasnt the last item
                following = current.next # move ahead to the next item
        llist.head = previous
        return llist

    def sum(self):
        list_sum = 0

        node = self.head

        while node is not None:
            list_sum += node.data
            node = node.next

        return list_sum



llist = LinkedList()
print(llist.printList())
first = Node(1)
llist.head = first
print(llist.printList())
second = Node(2)
third = Node(3)

first.next = second
second.next = third
llist.printList()

llist.reverse(llist)

llist.printList()
print(llist.sum())