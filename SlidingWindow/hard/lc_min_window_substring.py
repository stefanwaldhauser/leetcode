class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def c_to_index(c):
            if c.islower():
                return ord(c) - ord('a')
            else:
                return ord(c) - ord('A') + 26

        unique_chars_remaining = len(set(list(t)))
        t_count = [0] * 52
        for _, c in enumerate(t):
            t_count[c_to_index(c)] += 1

        window_count = [0] * 52

        min_length = float("inf")
        l_min = -1
        r_min = -1

        l = 0
        for r in range(len(s)):
            new_c = s[r]

            window_count[c_to_index(new_c)] += 1
            # The count has just gotten equal for the first time -> eliminated one char
            if t_count[c_to_index(new_c)] > 0 and t_count[c_to_index(new_c)] == window_count[c_to_index(new_c)]:
                unique_chars_remaining -= 1

            while unique_chars_remaining == 0:
                if r - l + 1 < min_length:
                    l_min = l
                    r_min = r
                    min_length = r - l + 1

                old_c = s[l]
                # The count was equal and now we destroy this equality for the first time again -> revived one char
                if t_count[c_to_index(old_c)] > 0 and t_count[c_to_index(old_c)] == window_count[c_to_index(old_c)]:
                    unique_chars_remaining += 1
                window_count[c_to_index(old_c)] -= 1
                l += 1

        if min_length == float("inf"):
            return ""
        else:
            return s[l_min: r_min + 1]


# Runtime: r always increases, l always increases -> no nested looping -> O(n) overall
# Space: O(1) as fixed alphabet
