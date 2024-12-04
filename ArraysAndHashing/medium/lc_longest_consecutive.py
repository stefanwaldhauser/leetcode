from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] = True

        longest_length = 0

        for num in num_count:
            # start of a sequence are the onces that are in num_count but that have not a previous one in it
            if num - 1 not in num_count:
                current_length = 0
                current_value = num
                while current_value in num_count:
                    current_length += 1
                    current_value += 1
                if current_length > longest_length:
                    longest_length = current_length

        return longest_length


# Runtime: O(n)
# Space: O(n)
