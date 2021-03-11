class Hashmap(object):
    
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.keys = [None] * self.size
        self.items = [None] * self.size
    
    def _hash(self, key):
        value = 0
        for letter in key:
            value += ord(letter)
        return value % self.size
    
    def _rehash(self, oldhash):
        return (oldhash + 1) % self.size
    
    def put(self, key, value):
        hash_value = self._hash(key)
        return_value = False
        if self.keys[hash_value] is None:
            self.keys[hash_value]= key
            self.items[hash_value]= value
            return_value = True
            self.count += 1
        else: # we have conflict
            rehash = self._rehash(hash_value)
            while (not self.keys[rehash] is None) and (rehash != hash_value):
                rehash = self._rehash(rehash)
                
            if self.keys[rehash] is None:
                self.keys[rehash] = key
                self.items[rehash] = value
                return_value = True
                self.count += 1
            else:
                return_value = False
        return return_value
    
    def get(self, key):
        init_hash = self._hash(key)
        hash_value = init_hash
        item = None
        exit_loop = False
        
        while (not self.keys[hash_value] is None) and (not exit_loop):
            if self.keys[hash_value] == key:
                item = self.items[hash_value]
                exit_loop = True
            else:
                hash_value = self._rehash(hash_value)
                if hash_value == init_hash:
                    exit_loop = True
        return item
    
    def delete(self, key):
        init_hash = self._hash(key)
        hash_value = init_hash
        item = None
        exit_loop = False
        while (not self.keys[hash_value] is None) and (not exit_loop):
            if self.keys[hash_value] == key:
                item = self.items[hash_value]
                self.items[hash_value] = None
                self.keys[hash_value] = None
                exit_loop = True
                self.count -= 1
            else:
                hash_value = self._rehash(hash_value)
                if hash_value == init_hash:
                    exit_loop = True
        return item
    
    def load(self):
        return self.count / float(self.size)
