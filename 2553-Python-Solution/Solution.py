class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
         return [int(char) for num in nums for char in str(num)]