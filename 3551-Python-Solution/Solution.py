class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        digit_sum = []
        for i in range(n):
            num = nums[i]
            temp = num
            total = 0
            while temp > 0:
                total += temp % 10
                temp //= 10
            digit_sum.append([total, num, i])

        digit_sum.sort()
        
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or digit_sum[i][2] == i:
                continue

            curr_idx = i
            while not visited[curr_idx]:
                visited[curr_idx] = True

                curr_idx = digit_sum[curr_idx][2]

                swaps += 1

            swaps -= 1
            
        return swaps