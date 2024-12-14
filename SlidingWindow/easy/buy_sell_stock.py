class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        cheapest_buy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - cheapest_buy
            max_profit = max([max_profit, profit])
            cheapest_buy = min([prices[i], cheapest_buy])
        return max_profit

# Runtime: O(n)
# Space: O(1)


class SlidingWindowSolution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # prices[l] is always the minimum price seen up to index r
        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            # found a smaller buy price then previous one so decrease window again to size 1 to keep invariant
            if profit < 0:
                l = r
        return max_profit

# Runtime: O(n)
# Space: O(1)
