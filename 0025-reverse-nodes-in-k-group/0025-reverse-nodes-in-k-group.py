# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy 

        while True:
            kth_node = group_prev
            count = 0 
            while kth_node and count < k:
                kth_node = kth_node.next
                count += 1 

            if not kth_node:
                break 

            next_group = kth_node.next

            prev_node = next_group
            current_node = group_prev.next

            count = 0
            while count < k:
                temp = current_node.next 
                current_node.next = prev_node
                prev_node = current_node
                current_node = temp
                count += 1

            last_node = group_prev.next
            group_prev.next = kth_node
            group_prev = last_node

        return dummy.next



