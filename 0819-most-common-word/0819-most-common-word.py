class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            max_count = 0
            max_count_word = ""
            delimeters = ['!','?', "'", "," , ";", "."]
            for delimeter in delimeters:
                paragraph = " ".join(paragraph.split(delimeter))
                # print(paragraph)
            
            words = paragraph.split()
            # print(words)
            word_dict = {}
            for word in words:
                word = word.lower()
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word] +=1
                    
            
            for word, freq in word_dict.items():
                if word in banned:
                    continue
                  # print(word, freq)
    
                else:
                    # print(word, freq)
                    if freq > max_count:
                        max_count = freq
                        max_count_word = word
                        
                    
                
                
            return max_count_word
                
                