class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = [] * len(A)
        for i in range(0, len(A)):
            result.append(len(list(set(A[:i+1]) & set(B[:i+1]))))       
        return result