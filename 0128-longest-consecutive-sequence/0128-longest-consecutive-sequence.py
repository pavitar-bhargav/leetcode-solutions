class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        X = set(nums)
        longest = 0
        for num in X:
            if num - 1 not in X:
                start_no = num
                length = 1

                while start_no + 1 in X:
                    start_no += 1
                    length += 1

                longest = max(longest , length)

        return longest


            

    