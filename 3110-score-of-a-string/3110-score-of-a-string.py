class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev  = ord(s[0])
        for i in range(1, len(s)):
            score += abs(prev - ord(s[i]))
            prev = ord(s[i])
        

        return score

        