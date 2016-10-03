# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        
        # p1 move n steps
        for i in xrange(n):
           p1 = p1.next
        
        # if move n steps is none, it means the 1st item should be removed.
        if not p1:
            return head.next
        
        # p1 and p2 move until the end
        while p1.next:
            p1 = p1.next
            p2 = p2.next
           
        # p2.next is the removed item, so remove it and link to the next one.
        p2.next = p2.next.next
        return head
       
       
