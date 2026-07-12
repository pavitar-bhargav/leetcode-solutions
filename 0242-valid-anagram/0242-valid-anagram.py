class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        oxford = {}
        for letter in s :
            if letter in oxford:
                oxford[letter] += 1
            else:
                oxford[letter] = 1
        for letter in t:
            if letter not in oxford or oxford[letter] == 0:
                return False
            else:
                oxford[letter] -= 1
        return True

        