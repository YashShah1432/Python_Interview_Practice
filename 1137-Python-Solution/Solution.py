class Solution:
    def tribonacci(self, n: int) -> int:
        result = []
        for i in range(0, n+1):
            if i == 0 or i == 1:
                result.append(i)
            elif i == 2:
                result.append(1)
            else:
                result.append(result[i-1] + result[i-2] + result[i-3]) 
        return result[n]