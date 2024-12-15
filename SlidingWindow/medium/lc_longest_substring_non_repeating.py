from collections import defaultdict

# Sliding window works here
#  It considers every possible ending position (r goes through entire string)
#  - For each ending position, it maintains the longest possible valid window that ends at that position
#  If we could start the window earlier (smaller l) while keeping it valid, the while loop wouldn't have moved l forward
#  If we need to start the window later(larger l) to be valid, the while loop ensures this
# At each position, we have the longest valid substring ending at that position, guaranteeing we won't miss the global maximum.

# The key insight is that we never miss a longer valid substring, as we always maintain the leftmost valid window ending at each position r, and by checking all positions r, we must encounter the optimal substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        chars = defaultdict(int)

        l = 0
        for r in range(len(s)):
            chars[s[r]] += 1

            # Shrink (by moving l) until we reach a valid window (the maximum valid window we can build with that r)
            while chars[s[r]] > 1:
                chars[s[l]] -= 1
                l += 1

            length = r - l + 1
            if length > max_length:
                max_length = length
        return max_length

# Runtime:
# - The outer loop runs exactly n times (right pointer)
# - The innter while loops total operations ACROSS all iterations of the outerloop is at most n because
#   it only moves forward, never backwards. It can never go beyond the right pointer. It can never go beyound the end of sthr eting
# In total therefore O(2n) = O(n)
# A simple way to understand this: each character can be added to the window once (by right pointer) and removed from the window at most once (by left pointer)
# , so each character is processed at most twice, giving us O(n) complexity.


# Space: O(n)
