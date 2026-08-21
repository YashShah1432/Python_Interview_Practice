class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum = 0
        odd_sum = 0
        for i in range(0, n*2, 2):
            even_sum += i
        for i in range(1, n*2, 2):
            odd_sum += i
        return math.gcd(even_sum, odd_sum)