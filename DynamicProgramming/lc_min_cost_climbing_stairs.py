from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        cost_last_step = cost[len(cost)-1]
        choice_a = self.minCostClimbingStairs(cost[:-1])
        choice_b = self.minCostClimbingStairs(cost[:-2])
        min_cost = min(choice_a, choice_b) + cost_last_step
        return min_cost
    def _minCost(self, cost: List[int], maxStep) -> int:
        if maxStep == 0:
            return cost[0]
        if maxStep == 1:
            return cost[1]
        
