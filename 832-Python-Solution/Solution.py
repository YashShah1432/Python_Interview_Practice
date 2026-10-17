class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        answer = []
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = 0 if image[i][j] == 1 else 1
            answer.append(image[i][::-1])
        return answer