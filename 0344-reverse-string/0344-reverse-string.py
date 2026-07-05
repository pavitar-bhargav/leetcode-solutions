class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
    
    # Keep swapping as long as the left pointer hasn't crossed the right pointer
        while left < right:
        # Step 1: Temporarily hold the left letter so we don't lose it
            temp = s[left]
        
        # Step 2: Overwrite the left letter with the right letter
            s[left] = s[right]
        
        # Step 3: Put our temporarily held letter into the right spot
            s[right] = temp
        
        # Step 4: Move both pointers one step closer to the middle
            left = left + 1
            right = right - 1
        