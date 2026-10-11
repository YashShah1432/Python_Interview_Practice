class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        answer = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if i == j or boxes[j] == "0":
                    continue
                else:
                    count = count + (abs(i-j))
            answer.append(count)
        return answer