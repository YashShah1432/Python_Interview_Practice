class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = []
        while n > 0:
            arr.append(n % 10)
            n = n // 10
        return math.prod(arr) - sum(arr) 