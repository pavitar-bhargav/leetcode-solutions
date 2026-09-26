class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ox = {}
        window = {}

        if len(s1) > len(s2):
            return False

        for s in s1:
            ox[s] = ox.get(s,0) + 1
        
        for i in range(len(s2)):
            char = s2[i]
            window[char] = window.get(char,0) + 1

            if i >= len(s1):
                left_char = s2[i-len(s1)]

                if window[left_char] == 1:
                    del window[left_char]
                else:
                    window[left_char] -= 1
            
            if ox == window:
                return True
        
        return False


        

    