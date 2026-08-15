class Solution(object):
    def truncateSentence(self, s, k):
        new_str = split(s)[:k]
        return " ".join(new_str)