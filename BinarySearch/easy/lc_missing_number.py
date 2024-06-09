from typing import List

#  https://leetcode.com/problems/missing-number/description/
#  n DISTINCT / UNIQUE numbers in the range [0, n]
#  Return the only number in the range that is missing from the array
#  1 <= n <= 10**4
#  If we sort the array, every number is in its index position until we hit index where
#  the number is missing, then we have a shift where number -1 = index.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        # First check this out of bound case. If its n its not at the last index (n is definitely shifted by 1 as one number is missing)
        if len(sorted_nums) != sorted_nums[len(sorted_nums) -1]:
            return len(sorted_nums) # n must be missing otherwise it would be at the last index
        # Now we can work with a search space that is inside the array bounds
        left = 0
        right = len(sorted_nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            num_mid = sorted_nums[mid]
            if num_mid != mid: # feasible solution but not minimum necessary
                right = mid
            else: #infeasible solution
                left = mid + +1
        return left


# Runtime: Sorting O(n log n) + Binary Search O(log n) =  O(n log n) as the sorting step dominates the overall runtime
# Space: O(n) for the sorted array + O(1) for binary search = O(n)


# XOR way
# Note x ^ x = 0
# 0 ^ x = x
# x ^ y = y ^ x

# Trick now is, if you have a long list of xors because of the third rule the order is irrelevant
# Now if you have a list with only duplicates you get 0 if you xor the whole list
# Now if there is one element added to that duplicates list, that has no partner the result of the xor
# will be this element because of the second rule
# Imagine we add the numbers from [0,...,n] and the actual numbers where one number is missing to a list
# If we then xor the whole list we get the number without a duplicate back :)

class BinarySolution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(0,n+1):
            xor = xor ^ i
        for i in nums:
            xor = xor ^ i
        return xor

# Runtime O(n)
# Space O(1)
