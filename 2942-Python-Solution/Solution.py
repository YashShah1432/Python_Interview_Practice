class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        count = -1
        for word in words:
            if word != word.replace(x, ""):
                count += 1
                result.append(count)
            else:
                count += 1
        return result

