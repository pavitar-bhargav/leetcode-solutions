class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_brackets = []
        
        bracket_pairs = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        
        for bracket in s:
            if bracket in bracket_pairs:
                if len(unclosed_brackets) > 0:
                    last_opened = unclosed_brackets.pop()
                else:
                    last_opened = None
                
                if bracket_pairs[bracket] != last_opened:
                    return False
            else:
                unclosed_brackets.append(bracket)
                
        return len(unclosed_brackets) == 0