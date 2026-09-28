class Solution:
    def maxDepth(self, s: str) -> int:
        current = 0
        depth = 0
        for bracket in s:
            if bracket == "(":
                current += 1
                if current > depth:
                    depth = current
            elif bracket == ")":
                current -= 1
        return depth

