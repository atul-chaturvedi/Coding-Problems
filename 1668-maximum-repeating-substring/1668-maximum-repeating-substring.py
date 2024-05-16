class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 1
        while word * ans in sequence:
            ans+=1
        
        return ans -1
#         window = len(word)
#         ans = 0
#         for i in range(len(sequence)):
#             count = 0
#             for start in range(i, len(sequence)-window +1):
#                 if word == sequence[start:start+window]:
#                     print(word, sequence[start:start+window], start, start+window)
#                     count +=1
#                     start += window
                    
#             ans = max(ans,count)
            
#             return ans


            
        