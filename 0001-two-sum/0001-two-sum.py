class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dom = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in dom:
                return [dom[diff], i]
            else:
                dom[nums[i]] = i
