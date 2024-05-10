class Solution:
    def isValid(self, word: str) -> bool:
        vowels_count =0
        consonants_count = 0
        word = word.lower()
        flag = True
        for char in word:
            if (char >='a' and char <= 'z'):
                if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
                    vowels_count+=1
                else:
                    consonants_count+=1
            elif char >='0' and char <='9':
                continue
            else:
                # print(char)
                flag = False
                
        # print(len(word) >= 3) 
        # print(flag)
        # print(vowels_count)
        # print(consonants_count)
        return len(word) >= 3 and flag and vowels_count and consonants_count
            
                
        