class Solution:

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels_found = []
        for i in range(len(s)):
            if (s[i] == 'a' or s[i] == 'A' 
                or s[i] == 'e' or s[i] == 'E' 
                or s[i] == 'i' or s[i] == 'I'
                or s[i] == 'O' or s[i] == 'o'
                or s[i] == 'u' or s[i] == 'U'):
                
                vowels_found.append(s[i])
                s[i] = 'found'
        
    
        vowels_found.reverse()
        
        index = 0
        for i in range(len(s)):
            if s[i]  == 'found':
                s[i] = vowels_found[index]
                index +=1
                
        s = "".join(s)
        return s
                
            
            
        
        