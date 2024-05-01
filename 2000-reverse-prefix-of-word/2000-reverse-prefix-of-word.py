class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        left =[]
        right = []
        for i in range(len(word)):
            if word[i] == ch:
                left = word[:i+1]
                right = word[i+1:]
                break
                
        
        if len(left) > 0:
            left = left[::-1]
            word = left + right
            
            
        word = "".join(word)
        return word
                
        