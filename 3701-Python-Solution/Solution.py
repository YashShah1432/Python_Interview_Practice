class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        temp = nums
        for i in range(1, len(nums), 2):
            temp[i] -= temp[i] * 2
        return sum(temp)