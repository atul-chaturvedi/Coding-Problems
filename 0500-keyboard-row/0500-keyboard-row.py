class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = Counter("qwertyuiop")
        r2 = Counter("asdfghjkl")
        r3 = Counter("zxcvbnm")
        
        ans = []
        
        for word in words:
            flag = True
            for letter in word:
                if letter.lower() in r1:
                    continue
                else:
                    flag = False
                    
            if flag:
                ans.append(word)
        
        
        for word in words:
            flag = True
            for letter in word:
                if letter.lower() in r2:
                    continue
                else:
                    flag = False
                    
            if flag:
                ans.append(word)
                
                
        for word in words:
            flag = True
            for letter in word:
                if letter.lower() in r3:
                    continue
                else:
                    flag = False
                    
            if flag:
                ans.append(word)
                
                
        return ans