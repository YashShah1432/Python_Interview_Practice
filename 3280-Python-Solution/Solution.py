class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split("-")
        result = []
        for num in arr:
            binary = bin(int(num))
            result.append(binary[2:])            
        return "-".join(result)