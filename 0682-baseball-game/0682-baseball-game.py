class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for ch in operations:
            if ch == '+':
                arr.append(arr[-1] + arr[-2])
            elif ch =='D':
                arr.append(arr[-1]*2)
            elif ch == 'C':
                arr.pop(-1)
            else:
                arr.append(int(ch))
        
        return sum(arr)
                
        