class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i, j = 0 , 0
        res = float('-inf')
        while ( j < len(s)):
            count[s[j]] = count.get(s[j],0) + 1
            lenn = j - i + 1
            maxx = max(count.values())
            diff = lenn - maxx

            while (diff > k):
                count[s[i]]-=1
                if count[s[i]] == 0:
                    del count[s[i]]
                i +=1
                lenn = j-i+1
                maxx = max(count.values(),default = 0)
                diff = lenn - maxx
            lenn = j-i + 1
            res= max(res, lenn)
            j+=1
        return res
            

        