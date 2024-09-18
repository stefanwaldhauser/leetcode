# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=binary-search


from typing import List

# nums is sorted in non-decreasing order (increasing or same)
# nums: [5,7,7,8,8,10] len = 6, target 8
# i:    [0,1,2,3,4,5 ]

# As duplicates would be right next to each other they span two positons
# Return [firstFoundPosition, lastFoundPosition]
# If there is only one, than the positions are the same
# If the target does not exist than return [-1,-1]


# Find first position x
# f(x) = is nums[x] < target
# We find the first where this is false (min position where this is false)

# find last position x:
# f(x) = is nums[x] <= target
# We find the last where this is true (max position where this is true)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        # Min Index where not smaller is true
        def find_first_where_not_smaller():
            l = 0
            # r never updated if no solution -> l will go larger and larger until equal to len(target)
            r = len(nums)

            while l < r:
                mid = l + (r-l) // 2
                is_smaller = nums[mid] < target

                if not is_smaller:
                    r = mid  # mid is possible solution but there could be smaller ones
                else:  # mid and everything smaller not a solution
                    l = mid + 1

            # if target is smaller than every element in the array, it will collapse to the first element
            # so we need the extra check that it really is the target
            if l < len(nums) and nums[l] == target:
                return l
            return -1  # Target not found

        # Max Index where smaller or equal
        def find_last_where_smaller_or_equal():
            l = -1  # l never updated if no solution -> r will go smaller and smaller until -1
            r = len(nums) - 1

            while l < r:
                mid = l + (r-l + 1) // 2
                is_smaller_or_equal = nums[mid] <= target

                # mid is possible solution but there could be larger ones
                if is_smaller_or_equal:
                    l = mid
                else:  # mid and everything larger is not a solution
                    r = mid - 1

            # if target is larger than every element in the array it will collapse to the last element therefore we need the extra check if its really target
            if r >= 0 and nums[r] == target:
                return r
            return -1  # Target not found

        first = find_first_where_not_smaller()
        last = find_last_where_smaller_or_equal()

        return [first, last]
