# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None

        while head:
            tmp = head
            head = head.next
            tmp.next = new_head
            new_head = tmp
            
        return new_head
        
        
