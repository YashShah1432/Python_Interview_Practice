class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        alice = nums[::2]
        bob = nums[1::2]
        arr = []
        for i in range(len(alice)):
            arr.append(bob[i])
            arr.append(alice[i])
        return arr       