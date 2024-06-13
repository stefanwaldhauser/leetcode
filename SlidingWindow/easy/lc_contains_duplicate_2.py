# https://leetcode.com/problems/contains-duplicate-ii/
# integer array nums
# integer k
# Find out if there are two distincti ndices i and j in the array such that nums[i] == nums[j] and the absolute difference between i and j is at most k
# This basically means that two value are same and their index difference is at most k
# So the same value but not further than k indices apart

from typing import List

# Brute Force Solution
class BruteForceSolution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        last_index = len(nums) - 1
        left = 0
        right = 1
        while left <= last_index and right <= last_index:
            while(abs(right - left) <= k and right <= last_index):
                if nums[left] == nums[right]:
                    return True
                right = right + 1
            left = left + 1
            right = left + 1
        return False
# Time Complexity: O(k * n)
# Space Complexity: O(1)

# Sliding Window Slution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Window is basically the last seen k elements
        # We will go over the array with a sliding window of size [0,k].
        # These elements are from the new element always at most k elements away
        # At the beginning of the for loop will contain elements from nums[i-k] to nums[i-1].
        # The distance from element at i-k to ti element at i is abs((i-k)-i) = k
        last_k_elements_window = set()
        for i, new_element in enumerate(nums):
            if new_element in last_k_elements_window:
                return True;
            last_k_elements_window.add(new_element)
            if len(last_k_elements_window) > k:
                oldest_element = nums[i-k]
                last_k_elements_window.remove(oldest_element)
        return False

# Time Complexity: O(n) as we only need a single pass over window elements
# Space Complexity: Set of size min(n,k) which is the size of the sliding windwo
