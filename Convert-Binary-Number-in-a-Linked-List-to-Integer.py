1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def getDecimalValue(self, head: Optional[ListNode]) -> int:
8        num = 0 
9        current = head
10    
11        while current :
12              num = num * 2 + current.val
13              current = current.next
14        return num 
15        