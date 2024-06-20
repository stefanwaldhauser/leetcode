# https://leetcode.com/problems/sliding-subarray-beauty/

# Integer array nums of n integers where  1 <= n <= 10**5 and -50 <= nums[i] <= 50
# Subarray size k where 1 <= k <= n
# The beauty of a subarray is defined as: 0 if there are fewer than x negative integers, xth smallest integer if there are at least x negative integers
# Return the beauty of all subbarys of length k in order


from typing import List


# Correct but time limit exceeded
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauty = []

        window = []
        neg_count = 0

        for i, v in enumerate(nums):
            window.append(v)
            if v < 0:
                neg_count += 1
            if len(window) > k:
                oldest_value = window.pop(0)
                if oldest_value < 0:
                    neg_count -= 1
            if len(window) == k:
                if neg_count < x:
                    beauty.append(0)
                else:
                    sorted_window = sorted(window)
                    beauty.append(sorted_window[x-1])
        return beauty

# Runtime is dominated by the sorting
# Runtime: Sorting a list of size (k) at each new index. Sorting kosts O(k * log(k)). So Overall O(n) * O(k * log(k))


# Solution: Notice that -50 <= nums[i] <= 50! So we can use coutning sort here to greatly reduce the runtime cost of the second term

class CountingSortSolution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauty = []

        # window_count[0] corresponds to the count of -50
        # window_count[50] corresponds to the count of 0
        # window_count[100] corresponds to the count of 50
        # To get the count for a value v, use window_count[v + 50]
        # To get the actual value from an index i in window_count, use i - 50

        window_count = [0] * 101  # Index range 0 to 100 to cover values from -50 to 50
        neg_count = 0  # Count of negative numbers in the current window
        window_size = 0  # Current size of the sliding window

        for i, v in enumerate(nums):
            # Update the sliding window with the new element
            window_size += 1
            if v < 0:
                neg_count += 1
            window_count[v + 50] += 1

            # If the window size exceeds k, remove the oldest element
            if window_size > k:
                window_size -= 1
                oldest_value = nums[i - k]
                if oldest_value < 0:
                    neg_count -= 1
                window_count[oldest_value + 50] -= 1

            # Once the window reaches the required size, calculate the subarray beauty
            if window_size == k:
                if neg_count < x:
                    beauty.append(0)
                else:
                    # Find the x-th smallest element in the window
                    # We have found the x-th smallest element when we have seen at least x elements smaller or equal
                    seen = 0  # Count of elements seen so far
                    for i, count in enumerate(window_count):
                        seen += count
                        if seen >= x:
                            beauty.append(i - 50)
                            break
        return beauty


# Runtime: O(n×min(x,101)) which simplifies to O(n) as 101 is a constant
# Space: O(n) for beauty
