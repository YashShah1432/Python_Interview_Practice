class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for number in range(num1, num2+1):
            if number < 100:
                continue
            else:
                num = str(number)
                for j in range(1, len(num)-1):
                    if (int(num[j]) > int(num[j-1]) and int(num[j]) > int(num[j+1])) or (int(num[j]) < int(num[j-1]) and int(num[j]) < int(num[j+1])):
                        waviness += 1
        return waviness                   