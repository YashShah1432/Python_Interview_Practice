class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        subsets = set()
        for i in range(1, len(tiles)+1):
            for combo in permutations(tiles, i):
                subsets.add("".join(combo))
        return len(subsets)
        