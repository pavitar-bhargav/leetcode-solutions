class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oxford = {}
        for index in range (len(nums)):
            num = nums[index]
            sub = target - num 
            if sub in oxford:
                return [oxford[sub], index]
            else:
                oxford[num] = index