class Solution(object):
    def containsDuplicate(self, nums):
        return False if len(nums) == len(set(nums)) else True