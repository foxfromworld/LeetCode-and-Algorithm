# Source : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Author : foxfromworld
# Date  : 21/01/2021
# Second attempt # use bisect_right

#             0  1  2    0   1   2      0   1   2
# matrix = [[ 1, 5, 9], [10, 11, 13], [12, 13, 15]]
# k = 8

# Round 1
# mid = (low (1) + high (15)) // 2 = 8
#             0  1  2         0   1   2      0   1   2      
# matrix = [[ 1, 5, | 9], [| 10, 11, 13], [| 12, 13, 15]]
# sum of indexes: 2 + 0 + 0 = 2 < k (8) ==> low = mid + 1

# Round 2
# mid = (low (9) + high (15)) // 2 = 12
#             0  1  2         0   1      2      0     1   2      
# matrix = [[ 1, 5, 9 | ], [ 10, 11, |  13], [ 12, | 13, 15]]
# sum of indexes: 3 + 2 + 1 = 6 < k (8) ==> low = mid + 1

# Round 3
# mid = (low (13) + high (15)) // 2 = 14
#             0  1  2         0   1   2         0     1     2      
# matrix = [[ 1, 5, 9 | ], [ 10, 11, 13 |  ], [ 12,  13, |  15]]
# sum of indexes: 3 + 3 + 2 = 8 "not" < k (8) ==> high = mid - 1

# Round 4
# mid = (low (13) + high (13)) // 2 = 13
#             0  1  2         0   1   2         0     1     2      
# matrix = [[ 1, 5, 9 | ], [ 10, 11, 13 |  ], [ 12,  13, |  15]]
# sum of indexes: 3 + 3 + 2 = 8 "not" < k (8) ==> high = mid - 1
# ==> low not <= high ==> stop the loop

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    low, high = matrix[0][0], matrix[-1][-1]
    while low <= high:
      mid = (low + high)//2
      sum_indexes = sum([bisect.bisect_right(row, mid) for row in matrix])
      if sum_indexes < k:
        low = mid + 1
      else:
        high = mid - 1
    return low

# Date  : 21/01/2021
# First attempt 

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    newList = []
    for row in matrix:
      newList += row
    newList.sort()
    return newList[k-1]
