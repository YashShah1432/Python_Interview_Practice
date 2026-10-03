class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        arr = []
        result = []
        for i in range(len(names)):
            arr.append([heights[i], names[i]])
            arr.sort(reverse=True)
        for j in range(len(arr)):
            result.append(arr[j][1])
        return result