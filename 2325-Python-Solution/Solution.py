class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_str = ''
        ans = ""
        for char in key:
            if char not in new_str and char != " ":
                new_str += char

        for i in range(len(message)):
            if message[i] == " ":
                ans += " "
            else:
                ans += chr(ord('a') + new_str.index(message[i]))
        return ans