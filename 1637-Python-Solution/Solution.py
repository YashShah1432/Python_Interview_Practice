class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        max_dist = float('-inf')
        for i in range(len(points)):
            arr.append(points[i][0])

        arr.sort()
        for i in range(len(arr)-1):
            if max_dist < arr[i+1] - arr [i]:
                max_dist = arr[i+1] - arr [i]

        return max_dist