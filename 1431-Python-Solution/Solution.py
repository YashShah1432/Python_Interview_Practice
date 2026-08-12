class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        highest = max(candies)
        for i in range(0, len(candies)):
            candies[i] += extraCandies
            if candies[i] >= highest:
                result.append(bool(True))
            else:
                result.append(bool(False))
        return result