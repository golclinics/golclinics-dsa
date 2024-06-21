class Stack_List:
    def __init__(self):
        self._items = []
        
    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self._items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self._items[-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._items)

class Stack_Tuple:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, data):
        self.head = (data, self.head)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None
        data = self.head[0]
        self.head = self.head[1]
        self.size -= 1
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.head[0]

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.size

    def __repr__(self):
        return str(self.head)


        
        
