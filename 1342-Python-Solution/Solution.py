class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num > 0:
            if num % 2 == 1:
                num -= 1
                count += 1
            if num > 0:
                num /= 2
                count += 1
        return count