class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        multiplier = 1
        
        while n > 0:
            # Take up to 8 keys for the current multiplier position
            total_pushes += min(n, 8) * multiplier
            n -= 8
            multiplier += 1
            
        return total_pushes