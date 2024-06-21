# https://leetcode.com/problems/minimum-size-subarray-sum/
# Positive integer nums where  1 <= nums[i] <= 10**4 and 1 <= nums.length <= 10**5
# Target where 1 <= target <= 10**9
# Find MINIMAL subarray length such that the subarray sum is at least target. If there is no such subarray return 0
from typing import List  # Import List for type hinting

# Imagine the array [4, 2, 2, 7, 8, 1, 2, 8 , 1, 0] and target is 8
# If we open the window:
# [] is not >= 8
# [4] is not >= 8
# [4,2] is not >= 8
# [4,2,2] IS >= 8. ===> Minimum length so far is 3
# Adding one more element to the right does not make sense as we would have a worse solution
# Removing one element from the right does not make sense as we already seen this subarray
# The one we have not see is we remove the element from the left
# [2,2] is not >= 8.
# Removing another element does not make sense as we dont have a solution, so lets add more to the right
# [2,2,7] is >= 8
# [2,7] is >= 8 => Minimum length so far is 3
# [7] is not <= 8


# a)If window is invalid, add elements to the right until valid -> go to b
# b)If window is valid, remove elements from the left until invalid -> go to a





class Solution:
   def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        min_length = float('inf')
        l = 0
        r = 0
        current_sum = 0
        n = len(nums)

        while r < n:
            current_sum += nums[r]

            # While valid, try to make it better and better by removing from the left side
            while current_sum >= target:
                min_length = min(min_length, r - l + 1)
                current_sum -= nums[l]
                l += 1
            # now invalid, add one element to the right and try this one
            r += 1

        return min_length if min_length != float('inf') else 0
