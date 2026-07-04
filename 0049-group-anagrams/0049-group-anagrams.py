class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for s in strs:
            x = ''.join(sorted(s))
            r[x].append(s)
        return list(r.values())    