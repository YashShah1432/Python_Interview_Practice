class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(prices)):
            discount_applied = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    answer.append(prices[i]-prices[j])
                    discount_applied = True
                    break
            if not discount_applied:
                answer.append(prices[i])
        return answer               