class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        n = len(garbage)
        g, p, m, total = 0, 0, 0, 0
        for i in range(n-1, 0, -1):
            if 'G' in garbage[i]:
                g = i
                break
        for i in range(n-1, 0, -1):
            if 'P' in garbage[i]:
                p = i
                break
        for i in range(n-1, -1, -1):
            if 'M' in garbage[i]:
                m = i
                break
        for i in range(g):
            total += travel[i]
        for i in range(p):
            total += travel[i]
        for i in range(m):
            total += travel[i]
        return total + len("".join(garbage))