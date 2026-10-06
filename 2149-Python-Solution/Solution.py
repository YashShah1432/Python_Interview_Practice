class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        result = []
        for ele in nums:
            positive.append(ele) if ele >= 0 else negative.append(ele)
        for i in range(int(len(nums)/2)):
            result.append(positive[i])
            result.append(negative[i])
        return result