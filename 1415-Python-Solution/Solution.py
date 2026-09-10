class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        chars = ['a', 'b', 'c']
        combinations = itertools.product(chars, repeat=n)
        items = [''.join(ele) for ele in combinations]
        for item in items:
            isRepeat = False
            for i in range(len(item)-1):
                if item[i] == item[i+1]:
                    isRepeat = True
                    break
            if not isRepeat:
                result.append(item)
                 
        if len(result) < k:
            return ""
        else:
            return result[k-1]  