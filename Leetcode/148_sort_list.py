# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import Queue as Q
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        middle = self.find_middle(head)
        second_start =  middle.next
        middle.next = None
        return self.merge(self.sortList(head),self.sortList(second_start))
    def find_middle(self,start):
        slow = fast = start
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def merge(self,head1,head2):
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        
        node.next = head1 or head2
        return dummy.next
        