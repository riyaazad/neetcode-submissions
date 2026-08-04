# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #if only 1 or 2 nodes
        if not head.next or not head.next.next: 
            return

        #1. SPLIT
        #need to find middle (1 fast pointer and 1 slow)
        #by the time p2 finishes, p1 will be in middle
        mid = end = head #both pointers start in beg at first

        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        p2 = mid.next #p2 is the beginning of the second half so right after mid
        mid.next = None #breaks the list into 2

        #2. REVERSE
        #p2->p3, use snip-move tactic
        prev = None
        while p2 and p2.next:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev #connects list to the original None between the lists

        #3. MERGE
        p1 = head
        while p1 and p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next #move inwards
            p2 = p2next



