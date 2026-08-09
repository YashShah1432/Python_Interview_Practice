class Solution(object):
    def runningSum(self, nums):
        result = []
        sum = 0 

        for num in nums:
            sum += num
            result.append(sum)
        
        return result