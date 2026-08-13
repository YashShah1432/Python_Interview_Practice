class Solution(object):
    def restoreString(self, s, indices):
        result = [''] * len(s)
        for i in range (0, len(s)):
            result[indices[i]] = s[i]
        return ''.join(result)