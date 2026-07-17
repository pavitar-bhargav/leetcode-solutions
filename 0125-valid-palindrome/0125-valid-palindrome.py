class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for letter in s:
            if letter.isalnum():
                word += letter.lower()

        reverse = word[::-1]
        if reverse == word:
            return True
        return False
        