class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pair = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    pair += 1
        return pair