from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indeces = defaultdict(set)

        for i,v in enumerate(numbers):
            indeces[v].add(i)

        for num in indeces:
            i = min(indeces[num])
            partner = target - num
            if partner in indeces:
                j = max(indeces[partner])
                if i < j:
                    return [i+1,j+1]
        return []


# Runtime O(n)
# Space O(n)


# BUT: Given the problem that numbers is sorted we can calculate this with space O(1)
# In two sum 1 the array is unsorted. A pointer solution (space O(1)) would mean you have to compare each number with every other number, leading to runtime O(n^2)
# NOW: we do NOT have to compare with every number

# Example with sorted array [2, 7, 11, 15], target = 9
#left = 0    # points to 2
# right = 3   # points to 15

# If current sum (2 + 15 = 17) > target (9)
# We know we need a smaller sum
# Since array is sorted, moving right pointer left will always give smaller sum
# Because next number on right will always be smaller than current right

# If current sum (2 + 7 = 9) < target (9)
# We know we need a larger sum
# Since array is sorted, moving left pointer right will always give larger sum
# Because next number on left will always be larger than current left


# Two pointers from ends is better then doing it with two pointers running from the left:
# - The sorted property gives us a crucial advantage: we can eliminate possibilities systematically
# - If sum is too large, we know ALL pairs with current right pointer will be too large
# - If sum is too small, we know ALL pairs with current left pointer will be too small
# - This property ensures we don't miss any potential pairs


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            looking_for = target - numbers[i]
            # Only look at numbers until we exceed what we're looking for
            for j in range(i + 1, n):
                if numbers[j] > looking_for:
                    break  # No need to look further since array is sorted
                if numbers[j] == looking_for:
                    return [i+1, j+1]  # 1-based indexing


# This works BUT is not O(n)

#numbers = [1, 2, 3, 4, 5], target = 20
# i = 0: check 2,3,4,5 (4 comparisons)
# i = 1: check 3,4,5 (3 comparisons)
# i = 2: check 4,5 (2 comparisons)
# i = 3: check 5 (1 comparison)
# Total = 10 comparisons > n(5)
# The total number of comparisons follows the arithmetic sequence pattern Sum = n(n-1)/2 in worst case
# Which can be bounded by O(n2)

class BestSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        # we are looking for [i,j] where i < j so it makes sense to start with the two extremes, i as the smallest
        # and j as the largest number to conquer the whole search space

        i = 0
        j = n - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum > target: # we are too large, moving i would mean even bigger, only option is making j smaller
                j -= 1
            elif current_sum < target: # we are too small, moving j would mean even smaller, only option is making i larger
                i += 1
            else:
                return [i+1,j+1] # as 1 indexed
        return [-1,-1]
