class GolDictionaryLinearProbe:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.keys = [None] * self.size
        self.count = 0

    def _hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        if self.load() == 1:
            print("The dictionary is full. Consider deleting items")
            return False
        # Check for None and deleted values
        if self.keys[hash_value] is None or self.keys[hash_value] is False:
            self.keys[hash_value] = key
            self.items[hash_value] = value
            self.count += 1
            return True
        rehash_value = self._rehash(hash_value)
        # Check for empty or deleted
        while rehash_value != hash_value:
            rehash_value = self._rehash(rehash_value)
            if self.keys[rehash_value] is None or self.keys[rehash_value] is False:
                self.keys[rehash_value] = key
                self.items[rehash_value] = value
                self.count += 1
                return True
        return False

    def _getter(self, key):
        """
        This returns the hash index for the key being searched
        It is used by the get and delete method
        """
        hash_value = self._hash(key)
        if self.keys[hash_value] == key:
            return hash_value

        rehash_value = self._rehash(hash_value)
        while rehash_value != hash_value:
            # When it hits a False it rehashes so we avoid missing next values
            rehash_value = self._rehash(rehash_value)
            if self.keys[rehash_value] == key:
                return rehash_value
            # This means it is empty
            if self.keys[rehash_value] is None:
                return -1
        return -1

    def get(self, key):
        hash_value = self._getter(key)
        if hash_value == -1:
            print("The element does not exist")
        return self.items[hash_value]

    def delete(self, key):
        hash_value = self._getter(key)
        if hash_value == -1:
            print("The element doesn't exist")
            return False

        print("The data being deleted has the following components:\n"
              "Key : {}\n"
              "Value : {}", self.keys[hash_value], self.items[hash_value])
        self.keys[hash_value] = False
        self.items[hash_value] = False
        self.count -= 1
        return True

    def load(self):
        return self.count / self.size

    def __repr__(self):
        main_str = "The items in the dictionary are :\n"
        for i in range(self.size):
            main_str += "{} -> {}, ".format(self.keys[i], self.items[i])
        return main_str


if __name__ == '__main__':
    class_dictionary = GolDictionaryLinearProbe(5)
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
    print("This put should fail due to load")
    class_dictionary.put("s006", "Failed put")

