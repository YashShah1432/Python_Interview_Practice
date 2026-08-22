class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        reverse_num = nums[::-1]
        left_sum = []
        right_sum = []
        answer= []
        for i in range(0, len(nums)):
            if i == 0:
                left_sum.append(0)
                right_sum.append(0)
            else:
                left_sum.append(left_sum[i - 1] + nums[i-1])
                right_sum.append(right_sum[i - 1] + reverse_num[i-1])
        
        for i in range(0, len(nums)):
            answer.append(abs(left_sum[i] - right_sum[len(nums)-i-1]))
        return answer