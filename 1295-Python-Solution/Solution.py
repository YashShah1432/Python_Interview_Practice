class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digit = 0
            if num >= 10:
                while num > 0:
                    digit += 1
                    num = num // 10 
                if digit % 2 == 0:
                    count += 1
        return count