class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        count = 0
        s = s[::-1]
        for char in s:
            if char == '-':
                continue
            else:
                if count == k:
                    ans += '-' + char
                    count =0
                else:
                    ans += char
                
                count+=1
                    
                    
    
        ans = ans[::-1]
        return ans.upper()
                    
                
        