#ttps://leetcode.com/problems/remove-element/
from typing import List

class MySolution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 # purpose is to locate elements that are equal to val
        right = len(nums) - 1 # purpose is to locate elements that are not equal to val

        # Do until left pointer exceeds right pointer. At this point all swaps have been completed.
        while left <= right:
            # Increases until it either finds a val or crosses right
            while left <= right and nums[left] != val:
                left += 1
            # Decreases until it either finds a non-val or crosses left
            while left <= right and nums[right] == val:
                right -= 1
            # If we did not cross, we must have a val and a non val to swap
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                # Adjust both pointers to continue scanning from the next position
                left +=1
                right -=1
        return left

# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space


# OK: This solution works because we do not care that the non-values are maintained
# All we basically care is that all the non-val values are moved to the front of the list
# You do NOT have to swap as you do not care about the val entries
class ReaderWriterPointers:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # loops over whole nums and tries to find non-vals that we write one by one into the spots of the next cell
        next_cell = 0 # spot where we write the next non-val value!

        # in our case we can write only non-val values! The reader moves one by one
        # and we stop and write if we encounter a non-val value.

        #Note: It could be the case that both i and the next_cell are at the same index. If i is then a non-val value, we will override the same value
        # with itself but thats not a problem.

        # Do until left pointer exceeds right pointer. At this point all swaps have been completed.
        while i <= len(nums) - 1:
            if nums[i] != val: # encountered a non-val value that we write
                if i != next_cell: # save writing cells to itself
                    nums[next_cell] = nums[i]
                i += 1
                next_cell += 1
            else: # encountered a val-value, not to write
                i += 1
        return next_cell


# Time Complexity: O(n)
# Space Complexity: O(1) as no extra space
