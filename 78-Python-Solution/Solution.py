class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = []
        for i in range(len(nums)+1):
            for combo in combinations(nums, i):
                subsets.append(list(combo))
        return subsets
            