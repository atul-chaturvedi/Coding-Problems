class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([word for word in s.split(" ") if len(word) > 0][-1])