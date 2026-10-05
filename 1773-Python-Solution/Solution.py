class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in range(len(items)):
            if (ruleKey == "type" and ruleValue == items[i][0]) or (ruleKey == "color" and ruleValue == items[i][1]) or (ruleKey == "name" and ruleValue == items[i][2]):
                count += 1
        return count