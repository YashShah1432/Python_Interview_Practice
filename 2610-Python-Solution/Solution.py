class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = []
        counts = Counter()
        
        for num in nums:
            row_index = counts[num]

            if row_index == len(result):
                result.append([])

            result[row_index].append(num)
            counts[num] += 1

        return result