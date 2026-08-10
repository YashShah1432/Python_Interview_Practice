class Solution(object):
    def maximumWealth(self, accounts):
        result = []
        for arr in accounts:
            sum = 0
            for num in arr:
                sum += num
            result.append(sum)
        return max(result)     