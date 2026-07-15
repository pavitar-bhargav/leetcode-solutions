class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = ""
        for value in s:
            if value.isalnum():
                original += value.lower()

        reverse = original[::-1]

        if original == reverse:
            return True
        return False
