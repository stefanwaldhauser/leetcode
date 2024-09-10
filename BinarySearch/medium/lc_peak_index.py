from typing import List


# Integer mountain array [0,1,0] of length n, where the values strictly increase to a peak element and then strictly decrease from that peak element
# [0,2,10]
# [0,10,5,2]
# Return the index of the peak element :)


# Question we ask on positon x: Is that an 'increase' from position x-1?
# What we are looking for is the maximum / last position where this question is true -> Binary search
# Note: We define the first element as always increasing to make it work if the peak is at index 0


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = l + (r-l + 1) // 2
            is_increase = (mid == 0 or arr[mid-1] < arr[mid])
            if is_increase:
                l = mid
            else:
                r = mid -1
        return l


# Runtime: O(log(n))
