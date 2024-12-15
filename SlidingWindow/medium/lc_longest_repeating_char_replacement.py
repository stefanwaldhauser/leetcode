from collections import defaultdict


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        candidates = set(s)
        longest = 0

        for c in candidates:
            other_chars = 0
            l = 0
            for r in range(len(s)):
                if s[r] != c:
                    other_chars += 1
                while other_chars > k:
                    if s[l] != c:
                        other_chars -= 1
                    l += 1
                longest = max([longest, (r-l) + 1])
        return longest

# Runtime:
# Max 26 candidates in the worst case (O(1))
# r always oves forward, l always moves forward -> O(n)
# O(n)
# Space:
# O(1) as max 26 in the candidates set


# To remove the O(26) part a better solution exist
class BestSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Track frequency of each char in current window
        char_count = defaultdict(int)
        # Track count of most frequent char in current window
        most_frequenct_char_count = 0
        max_length = 0   # Result: longest valid substring length
        left = 0        # Left pointer of sliding window

        for right in range(len(s)):
            # 1. Add new character to window
            char_count[s[right]] += 1

            # 2. We could have a new max char as we added s[right] += 1
            most_frequenct_char_count = max(
                most_frequenct_char_count, char_count[s[right]])

            # 3. Check if window is valid
            # The best character to convert everything to is the most frequent character
            # We need to replace all other characters
            # We can easily therefor calculate how many character we would need to replace
            # By calculating amount_of_chars_in_window (its length) - max_count_char

            all_chars_count = right - left + 1
            to_replace_count = all_chars_count - most_frequenct_char_count

            if to_replace_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length
