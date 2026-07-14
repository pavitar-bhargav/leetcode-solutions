class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ox = {}
        for s in strs:
            label = "".join(sorted(s))
            if label not in ox:
                ox[label] = []
            ox[label].append(s)
        return list(ox.values())