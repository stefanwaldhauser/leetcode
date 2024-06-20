# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


# integer array nums ex: [1,5,4,2,9,9,9]
# integer k ex: 3
# Find the maximum subarray sum of all subarrays that are of exactly length k, and have distinct elements
# Return 0 if none such subarrays exist

from collections import deque, defaultdict  # Import deque for efficient sliding window and defaultdict for automatic dictionary initialization
from typing import List  # Import List for type hinting

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0

        # Create a deque to represent the sliding window. O(1) to pop from left!
        # .remove in a list is O(n) in comparison
        window = deque()
        window_sum = 0

        # We will use a dict to efficiently check for duplicates in O(1), namely if the number of keys in this dict is equal to k
        # If not, the window is either not yet at size k OR we have found a duplicate and removed the key
        # Will contain the count of all elements currently in the window.
        # The trick is that the number of keys will be less than k if any element has a count different than 1, meaning a duplicate
        window_count = defaultdict(int)

        for v in nums:
            window.append(v)
            window_sum += v
            window_count[v] += 1 # This is no problem as we use defaultdict. If the key does not exist yet, it will be set to 0 before adding 1

            if len(window) > k:
                oldest_element = window.popleft()
                window_sum -= oldest_element
                window_count[oldest_element] -= 1
                if window_count[oldest_element] == 0: # All occurrences of that element removed from window, remove key
                    del window_count[oldest_element]

            # This checks if we have a window that has grown to size k and has no duplicates
            if len(window) == k and len(window_count) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum



# Run Time: O(n)
# Space Complexity: O(k)


# Solution without the queue
class Solution2:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0

        window_length = 0
        window_sum = 0
        window_count = defaultdict(int)

        for i,v in enumerate(nums):
            window_sum += v
            window_count[v] += 1
            window_length += 1

            if window_length > k:
                oldest_value = nums[i-k]
                window_sum -= oldest_value
                window_length -= 1
                window_count[oldest_value] -= 1
                if window_count[oldest_value] == 0:
                    del window_count[oldest_value]
            # Is the case when no duplicates and window grown to k
            if len(window_count) == k:
                max_sum = max(window_sum, max_sum)

        return max_sum
