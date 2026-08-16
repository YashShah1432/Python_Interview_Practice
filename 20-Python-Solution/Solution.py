class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) <= 1:
            return False
        else:
            for char in s:
                if char in ("(", "[", "{"):
                    stack.append(char)
                else:
                    if len(stack) > 0 and ((char == ")" and stack[len(stack)-1] == "(") or (char == "]" and stack[len(stack)-1] == "[") or (char == "}" and stack[len(stack)-1] == "{")):
                        stack.pop()
                    else:
                        return False
            return True if len(stack) == 0 else False