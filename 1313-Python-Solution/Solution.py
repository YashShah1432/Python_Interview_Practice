class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            while nums[i] > 0:
                result.append(nums[i+1])
                nums[i] -= 1
        return result