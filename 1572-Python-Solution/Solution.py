class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                if i == j:
                    result.append(mat[i][j])
        for i in range(0, len(mat)):
            for j in range(len(mat) - i -1, -1, -1):
                if i == j:
                    break
                else:
                    result.append(mat[i][j])
                    break
        return sum(result)