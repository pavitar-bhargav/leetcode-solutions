class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range (len(nums)):
            num = nums[i]
            diff = target - num
            if diff in dictionary:
                return [dictionary[diff], i]
            else:
                dictionary[num] = i