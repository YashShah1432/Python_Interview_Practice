class Solution(object):
    def reverseString(self, s):
        for i in range(0, len(s)):
            if i < len(s) - i:
                s[i], s[len(s) - i-1] = s[len(s) - i - 1], s[i]
        return s