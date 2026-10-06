class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] <= 9 and nums[i] == i:
                return i
            else:   
                total = 0             
                for digit in str(nums[i]):
                    total += int(digit)
                if total == i:
                    return i
        return -1