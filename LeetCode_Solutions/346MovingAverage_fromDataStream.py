# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 18/12/2020
# Second attempt 

  
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
    if length == self.divisor:
      self.queue.pop()
      self.queue.insert(0,val)
      return sum(self.queue)/self.divisor
    else: 
      self.queue.insert(0,val)
      return sum(self.queue)/(length+1)
