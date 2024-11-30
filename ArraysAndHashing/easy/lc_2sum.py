from typing import List


# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

# target = 10

# [4,5,6]
#  0 1 2

# solution [0, 2]


# Brute Force Solution:
# - For each i, loop over all other numbers j != i and see if they add up to target Runtime O(n^2), Space O(1)

# Smarter:

# Imagine you doing a loop over all numbers i. To check if i is part of the solution, we would need to know
# if target - nums[i] = nums[j] is in the array

# Solution: Store a dictionary all seen numbers and their index number[j] -> j
# For each number i in the loop check if there is an array entry for targert-nums[i], if exists you found the solution

# Runtime O(n)
# Space O(n)


# There are exactly two numbers in numbs that add up to target so nums[i] + nums[j] = target
# Return [i,j] (smaller index at 0)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = [-1, -1]
        num_to_index = {}
        for i, v in enumerate(nums):
            missing_num = target - v
            # Found solution
            if missing_num in num_to_index:
                for j in num_to_index[missing_num]:
                    # could happen because of duplicates in the array
                    if i < j:
                        solution = [i, j]
                    else:
                        solution = [j, i]
                    break
            # Found no solution yet
            num_to_index.setdefault(v, []).append(i)
        return solution


# Handling duplicates
# - The hash map (dictionary) approach abive automatically handles duplicates because we store the most recent index for each number!
# - Basically if you are at a 2, and you are looking for another 2, the one in the hashmap is guaranteed to be the most recent (to the left) one of the one I am currently at
# - If we need to find all possible pairs (not just the first one), we would need to modify the solution by iterating over all the indices in the array and summing up all soltuins
#
