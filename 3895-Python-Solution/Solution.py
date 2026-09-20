class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        string = ""
        for num in nums:
            string += str(num)
        
        count = 0
        for char in string:
            if char == str(digit):
                count += 1
        return count