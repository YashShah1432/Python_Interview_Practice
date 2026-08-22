class Solution:
    def maxFreqSum(self, s: str) -> int:
        char = Counter(s)
        vowel = [0]
        consonent = [0]
        for key, count in char.items():
            if key == 'a' or key == 'e' or key == 'i' or key == 'o' or key == 'u':
                vowel.append(count)
            else:
                consonent.append(count)
        return max(vowel) + max(consonent)