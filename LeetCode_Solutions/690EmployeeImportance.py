# Source : https://leetcode.com/problems/employee-importance/
# Author : foxfromworld
# Date  : 06/12/2020
# Second attempt 

class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    map = {item.id:item for item in employees}
    value = map[id].importance
    valueList = map[id].subordinates
    while valueList:
      sub = valueList.pop()
      value += map[sub].importance
      valueList += map[sub].subordinates
    return value

# Date  : 06/12/2020
# First attempt 

class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    map = {}
    for item in employees:
      map[item.id] = [item.importance,item.subordinates]
    value = map[id][0]
    valueList = map[id][1]
    while valueList:
      sub = valueList.pop()
      value += map[sub][0]
      valueList += map[sub][1]
    return value
