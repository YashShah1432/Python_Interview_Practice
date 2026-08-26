class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i in range(0, len(s)):
            total += abs(i - t.index(s[i]))
        return total