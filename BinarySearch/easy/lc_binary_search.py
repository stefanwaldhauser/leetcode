from typing import List

# https://leetcode.com/problems/binary-search/

class RecusiveSolution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums: List[int], target:int, left: int, right:int):
        if left > right:
            return -1
        # Ensures we round down to the actual index to the left of the halfway point
        # When the number of elements is odd than the right half is smaller by one element
        # This method efficiently reduces the problem space by half with each step, which is the core of binary search's logarithmic efficiency.
        # Note: If left == right. Then this will just be left == right == m!
        m = (left + right) // 2
        if nums[m] == target:
            return m
        if nums[m] < target: # Value must lay in (m, right]. If nums[m] is to small, everything to the left of m is definitely to small.
            return self._search(nums, target, m+1, right)
# Value must lay in [left, m). If nums[m] is to big, everything to the right of m is definitely to small.
        return self._search(nums, target, left, m-1)
