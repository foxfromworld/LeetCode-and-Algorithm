# Source : https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/
# Author : foxfromworld
# Date  : 30/03/2021
# Third attempt

class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    maxCnt = currCnt = prevVal = float('-inf')
    travIter = []
    modes = []
    while root: # Traverse left trees first
      travIter.append(root)
      root = root.left
    while travIter:
      currNode = travIter.pop()      
      currVal, right = currNode.val, currNode.right
      # Update the count      
      if currVal == prevVal: currCnt += 1
      else: currCnt = 1
      prevVal = currVal
      if maxCnt < currCnt:
        modes = [currVal]
        maxCnt = currCnt
      elif maxCnt == currCnt: modes.append(currVal)
      while right:
        travIter.append(right)
        right = right.left
    return modes

# Date  : 30/03/2021
# Second attempt

class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    maxCnt = currCnt = prevVal = float('-inf')
    travIter = []
    modes = []
    while root: # Traverse left trees first
      travIter.append(root)
      root = root.left
    while travIter:
      currNode = travIter.pop()      
      currVal, right = currNode.val, currNode.right
      # Update the count      
      if currVal != prevVal: currCnt = 1
      else: currCnt += 1
      prevVal = currVal
      if maxCnt == currCnt: modes.append(currVal)
      elif maxCnt < currCnt:
        modes = [currVal]
        maxCnt = currCnt
      while right:
        travIter.append(right)
        right = right.left
    return modes

# Date  : 29/03/2021
# First attempt

class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    dictMode = {}
    def traverse(node):
      if not node: return
      if node.val in dictMode:
        dictMode[node.val] += 1
      else:
        dictMode[node.val] = 1
      traverse(node.left)
      traverse(node.right)
    dictMode[root.val] = 1
    traverse(root.left)
    traverse(root.right)
    return [key for key, val in dictMode.items() if val == max(dictMode.values())]
