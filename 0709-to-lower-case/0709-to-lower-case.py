class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if ord(s[i]) >= 65 and  ord(s[i]) <= 90:
                s[i] = chr(int(ord(s[i]) + 32))
        
        s = "".join(s)
        
        return s
        