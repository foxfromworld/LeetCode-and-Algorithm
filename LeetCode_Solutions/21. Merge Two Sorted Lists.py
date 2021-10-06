# Source : https://leetcode.com/problems/merge-two-sorted-lists/
# Author : foxfromworld
# Date  : 06/10/2021
# Sedond attempt 

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# Date  : 06/10/2021
# First attempt 

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = temp = ListNode(0)
        while l1 != None and l2!= None:
            if l1.val <= l2.val:
                temp.next = l1
                l1= l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return new.next
