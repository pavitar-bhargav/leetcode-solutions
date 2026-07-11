class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ox = {}
        for i in range(len(nums)):
            if nums[i] in ox:
                return True
            else:
                ox[nums[i]] = 1
        return False