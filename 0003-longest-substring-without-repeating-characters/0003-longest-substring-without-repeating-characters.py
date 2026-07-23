class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ox = {}
        left = 0
        max_l = 0
        for i in range(len(s)):
            if s[i] in ox and ox[s[i]] >= left:
                left = ox[s[i]] + 1
            ox[s[i]] = i
            length = i - left + 1
            max_l = max(max_l, length)
        return max_l

        