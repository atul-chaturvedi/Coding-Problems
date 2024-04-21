class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub =""
        for char in s:
            sub +=char
            if len(s) != len(sub) and len(s) % len(sub) == 0:
                ans = [sub] * (len(s) // len(sub))
                ans = "".join(ans)
                # print(ans)
                if ans == s:
                    return True
        
        
        return False
        