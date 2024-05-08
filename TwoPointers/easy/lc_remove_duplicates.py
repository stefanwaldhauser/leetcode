#https://leetcode.com/problems/remove-element/
from typing import List
# Fast, Slow Pointer Based Approacj
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read_index = 0 # Finds the next unique element to write
        write_index = 0 # Points to the index to write the next unique element
        while read_index < len(nums):
            val = nums[read_index]
            nums[write_index] = val
            write_index += 1
            read_index += 1
            # Stop at the next unique element to write in the next iteration
            while read_index < len(nums) and nums[read_index] == val:
                read_index += 1
        return write_index

# Runtime: O(n)
# Extra Space: O(1) (in-place)
