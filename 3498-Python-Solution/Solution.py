class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_index = 0
        for i in range(0, len(s)):
            reverse_index += (ord('z') - ord(s[i]) + 1) * (i+1)
        return reverse_index        