class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        total = 0
        for i in range(len(tickets)):
            if i < k:
                total += tickets[i] if tickets[i] <= tickets[k] else tickets[k]
            elif i > k:
                 total += tickets[i] if tickets[i] <= tickets[k] - 1  else tickets[k] - 1               
            else:
                total += tickets[k]
        return total