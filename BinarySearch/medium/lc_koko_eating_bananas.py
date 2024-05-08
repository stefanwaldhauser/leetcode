# https://leetcode.com/problems/koko-eating-bananas/description/

# n piles of bananas in piles
# guards wille come back in h hours
# Koko can decide a bananas per hour eating rate of k
# Each hour she chooses SOME pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour from another pile

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.


# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

#Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Subproblem: Given a eating of speed of k, find minimum number of hours needed to eat the piles of bananas completely
# I think the best strategy is to eat first from all piles that are with piles[i] >= k to not waste any banana eating power. Then what is left
# is each entry that is either 0 or canb e eatin in one hour.



import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def eatPile(k):
            hours = 0
            for banana_pile_size in piles:
                hours += math.ceil(banana_pile_size/k)
            return hours
        searchSpaceMin = 1
        searchSpaceMax = max(piles) # There is no point in going higher than the highest pile in the piles as we can not eat from more than one pile in one hour!
        while searchSpaceMin < searchSpaceMax:
            searchSpaceMid = ((searchSpaceMax-searchSpaceMin)//2) + searchSpaceMin
            hoursNeeded = eatPile(searchSpaceMid)
            if hoursNeeded > h: # infeasible solution. Eating Speed definitely too low
                searchSpaceMin = searchSpaceMid + 1
            else: # feasible solution hours needed <= h. But could be not the optimum. Maybe we can go with a lowe eating speed
                searchSpaceMax = searchSpaceMid
        return searchSpaceMax


sol = Solution()
sol.minEatingSpeed([30,11,23,4,20], 20)
