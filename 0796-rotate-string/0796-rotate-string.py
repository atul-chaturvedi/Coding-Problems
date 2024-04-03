class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        
        while n >= 0:
            if s==goal:
                return True
            s = s[1:] + s[0]
            # print(n)
            n-=1
        
        return False
            
        