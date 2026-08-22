class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            total = 0
            while num > 0:
                d = num % 10
                num //= 10
                total += d
            result.append(total)
        return min(result)