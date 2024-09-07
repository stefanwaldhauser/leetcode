# https://leetcode.com/problems/valid-perfect-square/description/?envType=problem-list-v2&envId=binary-search

# Binary Search can be used

# Goal: Find the integer that squares to num if it exists

# Search Space: [0, num // 2] (expect for 0 and 1)
# If x * x > num than y > x means y * y > num
# If x * x < num than y < x means y * y < num

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0,1]: # 0 and 1 are perfect squares
            return True
        l = 0
        r = num // 2
        while l < r:
            mid = l + (r - l) // 2
            sqrt_mid = mid * mid
            if sqrt_mid == num:
                return True
            elif sqrt_mid > num:
                r = mid - 1
            else: # sqrt_mid < num
                l = mid + 1
        # Search Space Reduced to one Element that could be the solution or not
        return l * l == num

# Runtime: O(log(N))
# Space: O(1)
