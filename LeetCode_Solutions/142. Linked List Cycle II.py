# Source : https://leetcode.com/problems/linked-list-cycle-ii/
# Author : foxfromworld
# Date  : 16/03/2021
# Second attempt

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode: 
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        intersectNode = slow
        while intersectNode != head:
          intersectNode = intersectNode.next
          head = head.next
        return head
    return None 

# Date  : 16/03/2021
# First attempt

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    seen = set()
    while head:
      if head in seen:
        return head
      seen.add(head)
      head = head.next
    return None
