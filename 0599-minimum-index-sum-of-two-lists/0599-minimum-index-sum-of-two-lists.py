class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans =  []
        min_idx_sum = 1000000000
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    # print(f"{list1[i]} , {i}, {j}, {min_idx_sum}")
                    if i+j < min_idx_sum:
                        if len(ans) == 0:
                            ans.append(list1[i])
                        else:
                            ans = [list1[i]]
                        min_idx_sum = i+j
                    elif i+j == min_idx_sum:
                        ans.append(list1[i])
                        min_idx_sum = i+j
                        
                        
        return ans
                        