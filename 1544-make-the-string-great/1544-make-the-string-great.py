class Solution:
    def makeGood(self, s: str) -> str:
        flag = True
        
        while flag:
            flag = False
            # print(s)
            for i in range(len(s)-1):
                if i+1 < len(s) and s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    if len(s) > 2:
                        s = s[:i] + s[i+2:]
                    else:
                        s = ""
                    flag = True
                    break
                    
                    
            if len(s) == 0:
                flag = False
        
        return s
        