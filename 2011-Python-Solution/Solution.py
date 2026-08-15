class Solution(object):
    def finalValueAfterOperations(self, operations):
        result = 0
        for operation in operations:
            result += 1 if operation in ("++X", "X++") else -1
        return result