class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s[:])) != len(set(t[:])):
            return False
        
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                mp[s[i]] = t[i]
                
        
        return True