class Solution:
    def minimumPushes(self, word: str) -> int:
        collection = Counter(word)
        new_collection = dict(sorted(collection.items(), key=lambda item: item[1], reverse=True))
        n = len(new_collection)
        count = 0
        for index, (key, value) in enumerate(new_collection.items()):
            if index <= 7:
                count += collection[key]
            elif index > 7 and index <= 15:
                count += collection[key]*2
            elif index > 15 and index <= 23:
                count += collection[key]*3
            else:
                count += collection[key]*4
        return count