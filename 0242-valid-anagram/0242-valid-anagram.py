class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Anagram = {}      
        for letter in s:
            if letter in Anagram:
                Anagram[letter] += 1
            else:
                Anagram[letter] = 1
        for letter in t:
            if letter not in Anagram or Anagram[letter] == 0:
                return False
            Anagram[letter] -= 1
        return True 
