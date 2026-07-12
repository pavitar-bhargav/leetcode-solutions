class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            tag = ''.join(sorted(s))
            if tag not in dictionary:
                dictionary[tag] = []
            dictionary[tag].append(s)
        return list(dictionary.values())
        