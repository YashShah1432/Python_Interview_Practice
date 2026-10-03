class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) >= 26:
            result = []
            for char in sentence:
                result.append(ord(char))

            ans = set(result)
            final_ans = sorted(list(ans))
            return True if len(final_ans) == 26 else False            
        else:
            return False