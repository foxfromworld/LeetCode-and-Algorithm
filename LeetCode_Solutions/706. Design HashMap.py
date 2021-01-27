# Source : https://leetcode.com/problems/design-hashmap/
# Author : foxfromworld
# Date  : 27/01/2021
# Fourth attempt (Still not so fast)
# Reference: https://en.wikipedia.org/wiki/Hash_table

class Bucket:
  def __init__(self):
    self.bucket = []
  def insert(self, key, value):
    for i, entry in enumerate(self.bucket):
      if entry[0] == key:
        self.bucket[i][1] = value      
        return
    self.bucket.append([key, value])
  def search(self, key):
    for entry in self.bucket:
      if entry[0] == key:
        return entry[1]
    return -1
  def delete(self, key):
    for i, entry in enumerate(self.bucket):
      if entry[0] == key:
        del self.bucket[i]  
    return
class MyHashMap:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.size = 1747
    self.MyHashMap = [Bucket() for _ in range(self.size)]
  def put(self, key: int, value: int) -> None:
    """
    value will always be non-negative.
    """
    index = key % self.size
    self.MyHashMap[index].insert(key, value)
  def get(self, key: int) -> int:
    """
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    """    
    index = key % self.size
    return self.MyHashMap[index].search(key)
  def remove(self, key: int) -> None:
    """
    Removes the mapping of the specified value key if this map contains a mapping for the key
    """
    index = key % self.size
    return self.MyHashMap[index].delete(key)

# Date  : 27/01/2021
# Third attempt (Still not so fast)

class Bucket:
  def __init__(self):
    self.bucket = []
  def insert(self, key, value):
    for i, entry in enumerate(self.bucket):
      if entry[0] == key:
        self.bucket[i][1] = value
        isFound = True        
        return
    self.bucket.append([key, value])
  def search(self, key):
    for entry in self.bucket:
      if entry[0] == key:
        return entry[1]
    return -1
  def delete(self, key):
    for i, entry in enumerate(self.bucket):
      if entry[0] == key:
        del self.bucket[i]       
        return 
    return -1 
class MyHashMap:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.size = 3079
    self.MyHashMap = [Bucket() for _ in range(self.size)]
  def put(self, key: int, value: int) -> None:
    """
    value will always be non-negative.
    """
    index = key % self.size
    self.MyHashMap[index].insert(key, value)
  def get(self, key: int) -> int:
    """
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    """    
    index = key % self.size
    return self.MyHashMap[index].search(key)
  def remove(self, key: int) -> None:
    """
    Removes the mapping of the specified value key if this map contains a mapping for the key
    """
    index = key % self.size
    return self.MyHashMap[index].delete(key)


# Date  : 23/01/2021
# Second attempt (Still slow...)

class MyHashMap:
  def __init__(self):
    """
    Initialize your data structure here.
    """ 
    self.MyHashMap = []
  def put(self, key: int, value: int) -> None:
    """
    value will always be non-negative.
    """
    index = -1
    for i in range(len(self.MyHashMap)):
      if self.MyHashMap[i][0] == key:
        index = i
        self.MyHashMap[index][1] = value
        return
    self.MyHashMap.append([key, value])
  def get(self, key: int) -> int:
    """
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    """    
    index = -1
    for i in range(len(self.MyHashMap)):
      if self.MyHashMap[i][0] == key:
        index = i
        return self.MyHashMap[index][1]
    return -1
  def remove(self, key: int) -> None:
    """
    Removes the mapping of the specified value key if this map contains a mapping for the key
    """
    index = -1
    for i in range(len(self.MyHashMap)):
      if self.MyHashMap[i][0] == key:
        index = i
        return self.MyHashMap.pop(index)
    return -1  

# Date  : 23/01/2021
# First attempt (Really slow...)

class MyHashMap:
  def __init__(self):
    """
    Initialize your data structure here.
    """ 
    self.MyHashMap = []
  def put(self, key: int, value: int) -> None:
    """
    value will always be non-negative.
    """
    index = -1
    for i in range(len(self.MyHashMap)):
      if self.MyHashMap[i][0] == key:
        index = i
    print("~~",index,key)
    if index > -1:
      self.MyHashMap[index][1] = value
    else:
      self.MyHashMap.append([key, value])
  def get(self, key: int) -> int:
    """
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    """    
    index = -1
    for i in range(len(self.MyHashMap)):
      if self.MyHashMap[i][0] == key:
        index = i
    if index > -1:
      return self.MyHashMap[index][1]
    else:
      return -1
  def remove(self, key: int) -> None:
    """
    Removes the mapping of the specified value key if this map contains a mapping for the key
    """
    index = -1
    for i in range(len(self.MyHashMap)):
      if self.MyHashMap[i][0] == key:
        index = i
    if index > -1:
      return self.MyHashMap.pop(index)
    else:
      return -1          


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
