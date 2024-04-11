class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hm = Counter(s)
        
        for letter in t:
            if letter in hm:
                if hm[letter] > 0:
                    hm[letter] -=1
                else:
                    return letter
                
            else:
                return letter
        