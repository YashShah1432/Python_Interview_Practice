class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        dict_num = Counter(str(num) for num in nums)
        for key, count in dict_num.items():
            if count == 2:
                result.append(int(key))
        return result