# Source : https://leetcode.com/problems/reorder-data-in-log-files/
# Author : foxfromworld
# Date  : 21/02/2021
# Second attempt 

class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def getKey(log):
      id, log_ = log.split(' ',1)
      return (0, log_, id) if log_[0].isalpha() else (1, ) 
    return sorted(logs, key = getKey)

# Date  : 21/02/2021
# First attempt 

class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def getKey(log):
      id, log_ = log.split(' ',1)
      return (0, log_, id) if log_.replace(' ','').isalpha() else (1, ) 
    return sorted(logs, key = getKey)
