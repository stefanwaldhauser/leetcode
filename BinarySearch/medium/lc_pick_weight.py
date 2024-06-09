import random
from typing import List

# https://leetcode.com/problems/random-pick-with-weight/description/
# array w with POSITIVE integers. 0 indexed
# w[i] is the weight of the ith index
# pickIndex should randomly pick an in dex in the range [0, w.length-1] where the probabilty of picking is
# the weight of that index, so w[i]/sum(w)
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%)

class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.summed_weights = sum(w)
        # left inclusive, right exclusive [l,r)
        self.buckets = []
        left_border = 0
        for w in self.weights:
            right_border = left_border + w
            self.buckets.append([left_border, right_border])
            left_border = right_border
    def pickIndex(self) -> int:
        rand = random.randint(0, self.summed_weights - 1)
        for i, (left_border, right_border) in enumerate(self.buckets):
            if left_border <= rand < right_border:
                return i
        return -1  # In case no index is found, though logically it should always

# Runtime: Calculation sum O(n), bucket creatio O(n), Actual pick index O(n)


# Cumulative Sum Method
# We can do it with one number of each weight. Lets say for each i we calculate the weights up and including this w[i]
# What you get is a monotionically increasing list of cumulative weights.
# Now a number belongs in the bucket for index i if it fits below or equal to this cumulative weight.
# As there could be multiple such buckets we want to narrow it down to one by saying it has to be the smallest cumulative sum that fits or number
# (the first such number we encounter in the increasing number line)

class CumulativeSolution:

    def __init__(self, w: List[int]):
        self.total_sum = sum(w)
        self.cumulative_weights = []
        cumulative = 0
        for weight in w:
            cumulative = cumulative + weight
            self.cumulative_weights.append(cumulative)
    def pickIndex(self) -> int:
        rand = self.total_sum * random.random()
        # find the smallest meaning first cumulative sum it fits into
        for i, cumulative in enumerate(self.cumulative_weights):
            if rand < cumulative:
                return i

# To speed this up, we can do the searching of the right cumulative now via binary search

class CumulativeBinarySolution:

    def __init__(self, w: List[int]):
        self.total_sum = sum(w)
        self.cumulative_weights = []
        cumulative = 0
        for weight in w:
            cumulative = cumulative + weight
            self.cumulative_weights.append(cumulative)
    def pickIndex(self) -> int:
        rand = self.total_sum * random.random()
        left = 0
        right = len(self.cumulative_weights) - 1
        while left < right:
            mid = left + (right - left ) // 2
            if rand < self.cumulative_weights[mid]: # a solution but not necessarily the minimum
                right = mid
            else: # not a solution
                left = mid + 1
        return left

# In this way the runtime of pick index gets down to O(log n) from O(n)
