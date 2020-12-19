# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 19/12/2020
# Third attempt

class MovingAverage:
  def __init__(self, size: int):
    """
    Initialize your data structure here.
    """      
    self.window = size
    self.queue = [0]*self.window
    self.head = self.sum = 0
  def next(self, val: int) -> float:
    tail = (self.head+1) % self.window # keep the head and the tail
    self.sum = self.sum - self.queue[tail] + val # minus -> rotate the tail out and plus the new value
    self.queue[(self.head+1) % self.window] = val #Circular Queue
    self.head += 1
    return self.sum/min(self.head,self.window) 

# Date  : 19/12/2020
# Second attempt (slower)

class MovingAverage:
  def __init__(self, size: int):
    """
    Initialize your data structure here.
    """      
    self.window = size
    self.queue = [0]*size
    self.count = 0
  def next(self, val: int) -> float:
    self.queue[self.count%self.window] = val
    self.count+=1    
    return sum(self.queue)/min(self.count,self.window)
  
# Date  : 18/12/2020
# First attempt 

class MovingAverage:
  def __init__(self, size: int):
    """
    Initialize your data structure here.
    """      
    self.divisor = size
    self.queue = []
  def next(self, val: int) -> float:
    length = len(self.queue)
    if length == self.divisor:# lenght of queue == divisor
      self.queue.pop() # to keep to length of the list as the size of divisor
      self.queue.insert(0,val)
      return sum(self.queue)/self.divisor
    else: # lenght of queue < divisor
      self.queue.insert(0,val)
      return sum(self.queue)/(length+1)
