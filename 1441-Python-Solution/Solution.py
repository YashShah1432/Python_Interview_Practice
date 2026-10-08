class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        s = []
        length = min(max(target), n)
        for i in range(length+1):
            if i == 0:
                continue
            s.append("Push")
            if i not in target:
                s.append("Pop")
        return s