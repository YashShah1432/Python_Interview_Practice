class Solution(object):
    def convertTemperature(self, celsius):
        ans = []
        ans.append(round(celsius + 273.15, 5))
        ans.append(round(celsius * 1.80 + 32.00, 5))
        return ans