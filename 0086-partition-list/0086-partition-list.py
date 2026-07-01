# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head :
            return None
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        prev1 = dummy1
        prev2 = dummy2 

        current = head 

        while current :
            if current.val < x:
                prev1.next = current
                prev1 = current

            else:
                prev2.next = current
                prev2 = current

            current = current.next

        prev1.next = dummy2.next
        prev2.next = None

        head = dummy1.next
        return head