1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        nums.sort()
4        for i in range(len(nums)):
5            if nums[i] != i:
6                return i
7        return len(nums)  
8        
9            
10
11