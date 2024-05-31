class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor = xor ^ num
            
        rightmost_set_bit = xor & -xor
        
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1^=num
            else:
                num2^=num
        return [num1, num2]
            
        