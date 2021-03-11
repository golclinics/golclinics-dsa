class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __repr__(self):
        return "{} -> {}".format(self.key, self.value)


class GolDictionaryLL:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size
        self.count = 0

    def _hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        # Check for values
        if self.array[hash_value] is None:
            # If array position is empty
            self.array[hash_value] = Node(key, value)
        else:
            curr_node = self.array[hash_value]
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = Node(key, value)
        self.count += 1

    def get(self, key):
        # Gets the address
        hash_value = self._hash(key)
        curr_node = self.array[hash_value]
        if curr_node is None:
            # Element not found
            print("The element you are searching for doesn't exist")
            return None
        while curr_node.key != key:
            curr_node = curr_node.next
            if curr_node is None:
                print("The element you are searching for doesn't exist")
                return None
        return curr_node.value

    def delete(self, key):
        # Gets the address
        hash_value = self._hash(key)
        curr_node = self.array[hash_value]
        if curr_node is None:
            # Element not found
            print("The element you are searching for doesn't exist")
            return False
        previous_node = None
        while curr_node.key != key:
            previous_node = curr_node
            curr_node = curr_node.next
            if curr_node is None:
                print("The element you are searching for doesn't exist")
                return False
        self.count -= 1
        if previous_node is None:
            # Deleting the first element
            self.array[hash_value] = curr_node.next
            return True
        else:
            previous_node.next = curr_node.next
            return True

    def load(self):
        return self.count / self.size

    def __repr__(self):
        main_str = "The items in the dictionary are :\n"
        for i in range(self.size):
            main_str += "{} : ".format(i)
            curr_node = self.array[i]
            while curr_node is not None:
                main_str += "{}, ".format(curr_node)
                curr_node = curr_node.next
            main_str += "\n"
        return main_str


if __name__ == '__main__':
    class_dictionary = GolDictionaryLL(5)
    class_dictionary.put("s001", "Joshua")
    class_dictionary.put("s002", "George")
    class_dictionary.put("s003", "Collins")
    print(class_dictionary)
    class_dictionary.put("002s", "Joshua2")
    print("To test the put function")
    print(class_dictionary)

    print(class_dictionary.get("002s"))
    print(class_dictionary.get("s001"))
    print(class_dictionary.get("s002"))
    print(class_dictionary.get("s003"))
    print("Trying against an Index Error")
    print(class_dictionary.get("s004"))

    print("To test the delete operation")
    print(class_dictionary.delete("s002"))
    print(class_dictionary)

    print("Now we try and get the 002s element")
    print(class_dictionary.get("002s"))

    class_dictionary.put("s004", "Caleb")
    class_dictionary.put("s005", "Edwin")
    class_dictionary.put("s006", "Another Person")
    print(class_dictionary)
    print(class_dictionary.load())
