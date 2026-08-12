class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(0, n*2):
            if i % 2 == 0:
                result.append(nums[i // 2])
            else:
                result.append(nums[n + (i // 2)])
        return result       