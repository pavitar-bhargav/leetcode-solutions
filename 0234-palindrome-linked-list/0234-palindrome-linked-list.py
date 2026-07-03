# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head , head  
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        current = slow

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        left = head
        right = prev
        while right :
            if left.val != right.val :
                return False
            left = left.next
            right = right.next
        return True        
        
            


                

    
  