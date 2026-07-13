class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ox = {}
        for letter in s:
            if letter in ox:
                ox[letter] += 1
            else:
                ox[letter] = 1
        for letter in t:
            if letter not in ox or ox[letter] == 0:
                return False
            ox[letter] -= 1
        return True
        