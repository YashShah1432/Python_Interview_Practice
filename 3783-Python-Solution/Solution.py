class Solution:
    def mirrorDistance(self, n: int) -> int:
        num = 0
        temp = n
        while temp > 0:
            r = temp % 10
            temp //= 10
            num = (num * 10) + r
        return abs(n - num)