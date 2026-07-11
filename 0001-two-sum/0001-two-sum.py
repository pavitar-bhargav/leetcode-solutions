class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ox = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ox:
                return [ox[diff] , i]
            else:
                ox[nums[i]] = i
           
            