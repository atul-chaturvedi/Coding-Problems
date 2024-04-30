class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate =licensePlate.lower()
        licensePlate = list(licensePlate)
        hm = {}
        ans = ""
        for letter in licensePlate:
            if letter >= 'a' and letter <= 'z':
                if letter in hm:
                    hm[letter] +=1 
                else:
                    hm[letter] =1
                    
        
        for word in words:
            mp = Counter(word)
            flag = True
            for key, value in hm.items():
                if key in mp and mp[key] >= value:
                    continue
                else:
                    flag = False
                    
            if flag and (len(ans) == 0 or len(word) < len(ans)):
                ans = word
                
                    
        return ans
            
            
        
        