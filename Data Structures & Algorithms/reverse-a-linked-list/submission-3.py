# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# step 1: Save and Flip (SNIP)
# nxt = curr.next (Save the rest of the list so you do not lose it)
# curr.next = prev (Flip the arrow backward) 
# step 2: Shift Forward (MOVE)
# prev = curr (Drag prev up to curr)
# curr = nxt (Drag curr up to the saved nxt)
