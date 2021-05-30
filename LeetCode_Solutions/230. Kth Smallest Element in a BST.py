# Source : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Author : foxfromworld
# Date  : 30/05/2021
# First attempt 

class Solution:
  def kthSmallest(self, root, k):
    def inorder(node):
      return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    return inorder(root)[k - 1]
