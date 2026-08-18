class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        result = 0
        freq = Counter(str(n))
        for digit, frequency in freq.items():
            result += int(digit) * frequency
        return result