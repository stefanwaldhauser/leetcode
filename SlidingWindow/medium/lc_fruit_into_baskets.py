https://leetcode.com/problems/fruit-into-baskets/


# fruits is an integer array where 0 <= fruits[i] < fruits.length
# and 1 <= fruits.length <= 10**5
# fruits[i] is the type of fruit tree i produces
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.


# The two basket thing implies the subarrays we look for have <= 2 distinct values
# Out of those subarrays we have to find the longest
# ==> Find length of the longest subarray with <= 2 distinct values in it
# we use a dict to keep track of the count of elements in the window


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0
        fruit_type_count = defaultdict(int)
        l = 0
        r = 0

        while r < len(fruits):
            fruit_type_count[fruits[r]] += 1

            # while invalid shrink it
            while len(fruit_type_count) > 2 and l <= r:
                fruit_type_count[fruits[l]] -= 1
                if fruit_type_count[fruits[l]] == 0:
                    del fruit_type_count[fruits[l]]
                l += 1
            # valid
            max_length = max(max_length, r-l+1)
            r +=1
        return max_length
