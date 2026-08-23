class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dict_allowed = Counter(allowed)
        count = 0
        for word in words:
            isConsist = True
            dict_word = Counter(word)
            for key in dict_word:
                if key not in dict_allowed:
                    isConsist = False
                    break
            if isConsist:
                count += 1
        return count