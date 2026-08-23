class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        new_nums = []
        for i in range(nums[0], nums[len(nums)-1]+1):
            new_nums.append(i)
        result = list(set(new_nums) - set(nums))
        result.sort()
        return result