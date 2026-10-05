class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        result = []
        t = []
        v_idx = 0
        for i in range(len(s)):
            if s[i] in vowel:
                result.append(ord(s[i])-ord('A'))
        result.sort()
        for i in range(len(s)):
            if s[i] in vowel:
                t.append(chr(result[v_idx] + ord('A')))
                v_idx += 1
            else:
                t.append(s[i])
        return "".join(t)