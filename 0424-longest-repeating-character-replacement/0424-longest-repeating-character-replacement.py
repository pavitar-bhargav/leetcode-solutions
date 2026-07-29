class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ox = {}
        max_freq = 0
        left = 0
        longest = 0

        for i in range(len(s)):
            alpha = s[i]
            ox[alpha] = ox.get(alpha, 0) + 1
            max_freq = max(max_freq, ox[alpha]) 

            window_size = i - left + 1
            if window_size - max_freq > k:
                ox[s[left]] -= 1
                left += 1
            longest = max(longest , i - left + 1)
        return longest
                
        