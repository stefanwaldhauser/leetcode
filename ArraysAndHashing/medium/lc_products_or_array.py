# to calculate solution[i] we need to multiple all indices except i, which means all to the left of i and all to the right of i


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product, right_product = [0] * len(nums), [0] * len(nums)

        # Need to be 1 as it is the neural element of multiplication (has no effect)
        l_total, r_total = 1, 1
        l, r = 0, len(nums) - 1

        # O(2n)
        while l <= len(nums) - 1 and r >= 0:
            left_product[l] = l_total
            right_product[r] = r_total
            l_total *= nums[l]
            r_total *= nums[r]
            l += 1
            r -= 1

        solution = [0] * len(nums)
        # O(n)
        for i in range(len(nums)):
            solution[i] = left_product[i] * right_product[i]
        return solution

# Runtime O(n)
# Space O(n)

# Improved: Just do everything in one array, first the left pass and the right pass


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Left products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Right products
        postfix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
