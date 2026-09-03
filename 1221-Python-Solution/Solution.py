class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_count = 0
        balance = 0
        
        for char in s:
            # Increment for 'L', decrement for 'R' (or vice-versa)
            if char == 'L':
                balance += 1
            else:
                balance -= 1
                
            # If balance is 0, we've found a balanced substring
            if balance == 0:
                balanced_count += 1
                
        return balanced_count