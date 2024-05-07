# https://leetcode.com/problems/contains-duplicate/description/
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# Note: Set is implemented in python as a hash table so lookup/insert/delete takes O(1)
# Time : O(n) where n is the lenght of nums
# Space: O(n) where n is the length of nums
