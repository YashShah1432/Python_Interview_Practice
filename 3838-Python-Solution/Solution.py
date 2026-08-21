class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mod_arr = "" 
        for word in words:
            weight = 0
            for char in word:
                weight += weights[ord(char) - ord('a')]
            mod = weight % 26
            letter = chr(ord('z') - mod)
            mod_arr += letter
        return mod_arr