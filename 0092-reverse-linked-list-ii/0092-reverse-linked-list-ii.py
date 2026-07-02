# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right :
            return head 
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy 

        for i in range (left-1):
            prev = prev.next 
        current = prev.next

        for i in range (right - left):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

        head = dummy.next
        return head             

        