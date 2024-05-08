from typing import List

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.

# Goal: Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Example:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
 #Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
#2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.



# Imagine we try out a number say x
# If we notice we need more than 5 days we know its not a feasible solution and any weight BELOW x is also not a feasible solution
# If we notice we can do it within 5 days we know it is a the most mimum feasible solution we have seen so far but there could be better.
# Monotonicity => Use Binary Seach


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def calcDaysNeeded(shipCapacity):
            daysNeeded = 0
            shipWeight = 0
            for index, weight in enumerate(weights):
                if weight > shipCapacity:
                    return -1
                if shipWeight + weight > shipCapacity:
                    daysNeeded += 1
                    shipWeight = weight
                else:
                    shipWeight += weight
            daysNeeded += 1 # for the weight from the last index
            return daysNeeded


        searchSpaceMin = 1
        searchSpaceMax = sum(weights) # We could do it definitely in 1 day then. Another max would be n * 500. As maximum n elements in weights and max weight of each is 500. Would help us avoid this extra loop

        # Stops once search space is collapsed
        while searchSpaceMin < searchSpaceMax:
            searchSpaceMid = ((searchSpaceMax - searchSpaceMin) // 2) + searchSpaceMin
            daysNeeded = calcDaysNeeded(searchSpaceMid)
            if daysNeeded == -1 or daysNeeded > days:
                searchSpaceMin = searchSpaceMid + 1
            else:
                searchSpaceMax = searchSpaceMid
        return searchSpaceMax
