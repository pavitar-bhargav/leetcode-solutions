class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dix = {}
        for num in nums:
            if num in dix:
                return True
            else:
                dix[num] = 1
        return False
