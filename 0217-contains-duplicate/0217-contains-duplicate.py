class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ox = set()
        for num in nums:
            if num in ox:
                return True
            else:
                ox.add(num)
        return False
