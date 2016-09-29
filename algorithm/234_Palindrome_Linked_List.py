# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 
# ex: 12321, 1234321
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
            
        # find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half
        p = slow.next
        last = None
        while p:
            next = p.next
            p.next = last
            last = p
            p = next
            
        # check palindrome
        p1 = last
        p2 = head
        while p1:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
                
        return True
