from typing import List


# Very good application of monotonic stack. See  https://medium.com/@keshavrathinavel/leetcodes-monotonic-stack-problems-and-how-to-solve-them-made-easy-1c73c2d6d437
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        solution = prices.copy()

        for i in range(len(prices)):
            # found a next smaller or equal price to the stack top:
            while stack and prices[i] <= prices[stack[-1]]:
                popped = stack.pop()
                solution[popped] = solution[popped] - prices[i]
            stack.append(i)  # no solution yet

        return solution
