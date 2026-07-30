# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() #dummy points to beginning of list (aka right before first value and node is the pointer that can move along this list)

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1 #move to next value in l1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            node = node.next #now move pointer to next blank in the list we're creating
        
        node.next = list1 or list2 #in case one list is null

        return dummy.next #since dummy acc points before first acc value
        