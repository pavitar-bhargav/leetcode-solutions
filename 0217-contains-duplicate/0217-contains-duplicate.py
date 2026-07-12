class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dix = {}
        for i in range (len(nums)):
            num = nums[i]
            if num in dix:
                return True
            else:
                dix[num] = []
        return False
