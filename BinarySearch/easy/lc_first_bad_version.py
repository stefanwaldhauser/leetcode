from typing import List

# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# All the versions AFTER a version are also bad.
# [GOOD,GOOD,GOOD,GOOD,BAD,BAD,BAD]
# [0,   1   , 2  , 3  , 4 , 5 , 6]

# Find the First/ MINIMUM bad one, in this case 4

# We can use binary search here because if we have a GOOD one. we now everything left to it is also good and if we have a bad one
# we now everything right to it is a bad one.

def isBadVersion(x):
    return x == 2

class Solution:



    def firstBadVersion(self, n: int) -> int:
        searchSpaceMin = 1
        searchSpaceMax = n

        # search space not yet collapsed to 1 element
        while searchSpaceMin < searchSpaceMax:
            searchSpaceMid =  ((searchSpaceMax - searchSpaceMin) // 2) + searchSpaceMin
            if isBadVersion(searchSpaceMid): # searchSpaceMid is a feasible solution, but not necessarily the optimal one. Do not look to the right as they are worse (larger index)
                searchSpaceMax = searchSpaceMid
            else: # seachSpaceMid is a non feasible solution. Do not look to the left as they are definitely also non feasible
                searchSpaceMin = searchSpaceMid + 1
        return searchSpaceMax
