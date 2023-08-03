class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) ==0):
            return []
        numpad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        
        def help(digits, index, curr):
            if(index >= len(digits)):
                ans.append(curr)
                return
            
            for ch in numpad[ord(digits[index])-ord('0')]:
                help(digits, index+1, curr + ch)
                
        help(digits, 0, "")
        
        return ans
        
        