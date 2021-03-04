# Source : https://leetcode.com/problems/middle-of-the-linked-list/
# Author : foxfromworld
# Date  : 04/03/2021
# First attempt 

class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    middle = fast = head
    
    while fast and fast.next:
      print(fast.val)
      middle = middle.next
      fast = fast.next.next
    return middle
