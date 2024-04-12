class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = Counter(magazine)
        
        for letter in ransomNote:
            if letter in hm:
                if hm[letter] <=0:
                    return False
                else:
                    hm[letter] -=1
            else:
                return False
        
        return True