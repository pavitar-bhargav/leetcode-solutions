class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ox = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in ox:
                return ox[diff], i
            else:
                ox[num] = i
                
        
                
        

                


            