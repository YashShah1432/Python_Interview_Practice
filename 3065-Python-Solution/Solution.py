class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        while len(nums) and min(nums) < k:
            count += 1
            nums.remove(min(nums))
        return count