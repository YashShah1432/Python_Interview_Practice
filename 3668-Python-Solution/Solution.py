class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        not_in_list = list(set(order) - set(friends))
        for num in not_in_list:
            order.remove(num)
        return order