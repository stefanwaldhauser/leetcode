# Given a string s where 1 <= s.length <= 5 * 10**4
# Given integer k where 0 <= k <= 50
# Find the length of the longest substring of s that contains <= k DISTINCT characters


# Distinct means basically only the first occurence of a character counts


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Subarray that contains <= 0 distinct characters can only have length 0
        if k == 0:
            return 0
        # Find longest subarray that contains not more (<= ) than k distinct characters

        longest_subarray = 0
        distinct_chars = 0
        window_ascii_count = [0] * 128

        l = 0
        r = 0

        while r < len(s):
            r_ascii = ord(s[r])
            if window_ascii_count[r_ascii] == 0:
                distinct_chars += 1
            window_ascii_count[r_ascii] += 1

            # Make smaller if invalid
            while distinct_chars > k:
                l_ascii = ord(s[l])
                window_ascii_count[l_ascii] -= 1
                if window_ascii_count[l_ascii] == 0:
                    distinct_chars -= 1
                l += 1

            # Now longest possible valid solution with that current value of r
            longest_subarray = max(longest_subarray, r - l + 1)
            r += 1

        return longest_subarray

# Each character is added to the window once (when r moves right) and removed from the window once (when l moves right).
# This means each character in the string s is processed a constant number of times, leading to an overall linear time complexity.
# Runtime: O(2n) = O(n)
# Space: O(1) due to the fixed size of the ascii array


# If we use a dictionary we could support more than ascii
class NonAsciiSolution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        longest_subarray = 0
        char_count = {}
        l = 0

        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1

            while len(char_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

            longest_subarray = max(longest_subarray, r - l + 1)

        return longest_subarray
