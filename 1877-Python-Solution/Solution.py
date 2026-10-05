class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        nums.sort()
        result = []
        for i in range(n):
            result.append(nums[i]+nums[len(nums)-i-1])
        return max(result)
            