# Source : https://leetcode.com/problems/design-hashmap/
# Author : foxfromworld
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
