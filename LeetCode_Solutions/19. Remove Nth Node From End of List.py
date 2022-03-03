# Source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Author : foxfromworld
# Date   : 03/03/2022
# Second attempt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        last = dummy
        first = head
        while n > 0 and first:
            first = first.next
            n -= 1
        while first:
            first = first.next
            last = last.next
        last.next = last.next.next
        return dummy.next
    
# Date   : 03/03/2022
# First attempt

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        copy = head
        while copy:
            copy = copy.next
            length += 1
        if length == 1 and n == 1: return None
        if length == n: return head.next
        length = length - n -1
        copy = head
        while length > 0:
            length -= 1
            copy = copy.next
        copy.next = copy.next.next
        return head
