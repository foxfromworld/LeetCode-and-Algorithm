# Source : https://leetcode.com/problems/linked-list-cycle/
# Author : foxfromworld
# Date  : 16/03/2021
# First attempt #set is faster than list

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    seen = set()
    while head:
      if head in seen:
        return True
      else:
        seen.add(head)
      head = head.next
    return False  

# Date  : 16/03/2021
# First attempt #very slow

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    seen = []
    while head:
      if head in seen:
        return True
      else:
        seen.append(head)
      head = head.next
    return False
