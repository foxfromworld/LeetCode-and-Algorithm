# Source : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Author : foxfromworld
# Date  : 30/05/2021
# Second attempt 

class Solution:
  def kthSmallest(self, root, k):
    stack = []
    while True:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      k -= 1 
      if k == 0:
        return root.val
      root = root.right

# Date  : 30/05/2021
# First attempt 

class Solution:
  def kthSmallest(self, root, k):
    def inorder(node):
      return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    return inorder(root)[k - 1]
