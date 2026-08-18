class Solution:
    def maxDistinct(self, s: str) -> int:
        result = []
        for char in s:
            result.append(char)
        return len(set(result))