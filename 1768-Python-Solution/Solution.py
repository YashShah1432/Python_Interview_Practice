class Solution(object):
    def mergeAlternately(self, word1, word2): 
        max_length = max(len(word1), len(word2))
        merged = ""
        for i in range(0, max_length):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
        return merged