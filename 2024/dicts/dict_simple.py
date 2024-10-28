
class SimpleDict(object):
  def __init__(self, cap=50):
    self.store = [None]*cap
    self.n = 0
  
  def insert(self, x):
    # check for duplicates
    s = self.search(x)
    if s >= 0:
      return s
    
    self.store[self.n] = x
    self.n += 1
    return self.n - 1
  
  def search(self, k):
    for i in range(len(self.store)):
      if self.store[i] == k:
        return i
    return -1

  def delete(self, x):
    # assumption: item must already have been found
    self.store[x] = self.store[self.n - 1]
    self.n -= 1
    self.store[self.n] = None

  # for debug purposes
  def __str__(self):
    return str(self.store) + f" size: {self.n}"
  
  def min(self):
    min_ = 0
    for i in range(1, self.n):
      if self.store[i] < self.store[min_]:
        min_ = i
    return min_
  
  def max(self):
    max_ = 0
    for i in range(1, self.n):
      if self.store[i] > self.store[max_]:
        max_ = i
    return max_
  
  def predecessor(self, x):
    # c -- candidate
    # get first value less than store[x] - store[c]
    # and then look for store[i] > store[f] but < store[x]
    # if found c = i
    # return c
    c = -1
    for i in range(self.n):
      if  self.store[i] < self.store[x]:
        if c < 0:
          c = i
        elif self.store[i] > self.store[c]:
          c = i
    return c


  def successor(self, x):
    # get first value greater than store[x] - store[c]
    # and then look for store[i] < store[c] but > store[x]
    # if found c = i
    # return c
    c = -1
    for i in range(self.n):
      if  self.store[i] > self.store[x]:
        if c < 0:
          c = i
        elif self.store[i] < self.store[c]:
          c = i
    return c

# tests
d = SimpleDict()

d.insert(20)
d.insert(40)
d.insert(10)
d.insert(60)

print(d)

d.delete(1)

print(d)

d.insert(100)

print(d.max(), d.min())

print(d.predecessor(0))
print(d.predecessor(2))
print(d.successor(2))
