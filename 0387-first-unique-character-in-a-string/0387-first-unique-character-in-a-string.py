class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = Counter(s)
        
        for i in range(len(s)):
            if hm[s[i]] ==1:
                return i
            
        
        
        return -1
                
        