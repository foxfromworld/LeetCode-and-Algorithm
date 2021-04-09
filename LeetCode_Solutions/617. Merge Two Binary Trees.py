# Source : https://leetcode.com/problems/merge-two-binary-trees/
# Author : foxfromworld
# Date  : 09/04/2021
# Second attempt 

class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1: return t2
    if not t2: return t1
    stack = [[t1, t2]]
    while stack:
      currPair = stack.pop()
      if not currPair[1]:
        continue
      currPair[0].val += currPair[1].val
      if not currPair[0].left:
        currPair[0].left = currPair[1].left
      else:
        stack.append((currPair[0].left, currPair[1].left))
      if not currPair[0].right:
        currPair[0].right = currPair[1].right
      else:
        stack.append((currPair[0].right, currPair[1].right))
    return t1
# Date  : 09/04/2021
# First attempt 

class Solution:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1: return t2
    if not t2: return t1
    t1.val = t1.val + t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1
