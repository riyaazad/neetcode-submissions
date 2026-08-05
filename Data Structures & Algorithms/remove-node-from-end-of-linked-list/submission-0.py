# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #1. find length
        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next

        #2. iterate to right before "nth" node in list
        removeIndex = length - n

        #if we need to remove first element
        if removeIndex == 0:
            return head.next

        curr = head
        for i in range(removeIndex - 1): 
            curr = curr.next
        curr.next = curr.next.next
        return head

        #     if (i+1) == removeIndex: #since we stopped i right before the node we need to remove
        #         curr.next = curr.next.next
        #     curr = curr.next
        # return head



        