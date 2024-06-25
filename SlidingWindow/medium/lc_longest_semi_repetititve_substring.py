# 1 <= s.length <= 50
# '0' <= s[i] <= '9

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_length = 0
        l = 0
        r = 0
        no_adjacent_duplicates = 0


        while r < len(s):
            if r - 1 >= 0 and s[r-1] == s[r]:
                no_adjacent_duplicates += 1
            # if invalid shrink it
            # I dont have to check l < r here as it will become valid
            # before l > r can happen
            while no_adjacent_duplicates > 1:
                if l + 1 < len(s) and s[l+1] == s[l]:
                    no_adjacent_duplicates -= 1
                l += 1
            # now guaranteed to be valid
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

# Runtime: O(n)
# Space: O(1)
