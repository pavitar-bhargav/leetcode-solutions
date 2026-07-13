class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ox = {}
        for num in nums:
            
            if num in ox:
                ox[num] += 1
            else:
                ox[num] = 1
        sorted_ox = sorted(ox, key = lambda num : ox[num], reverse = True)
        return sorted_ox[:k]