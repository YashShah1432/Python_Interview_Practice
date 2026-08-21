class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        for i in range(1, len(nums) + 1):
            for combo in combinations(nums, i):
                subset.append(reduce(operator.xor, combo))
        return sum(subset)