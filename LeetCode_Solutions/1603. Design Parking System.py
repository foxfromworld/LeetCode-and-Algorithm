# Source : https://leetcode.com/problems/design-parking-system/
# Author : foxfromworld
# Date  : 13/05/2021
# First attempt

class ParkingSystem:
  def __init__(self, big: int, medium: int, small: int):
    self.slots = [big, medium, small]    
  def addCar(self, carType: int) -> bool:
    if self.slots[carType - 1]  > 0:
      self.slots[carType - 1] -= 1
      return True
    else:
      return False
