class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = 0

        num_chars_missing = 0
        chars_missing = {}

        for i in range(len(s1)):
            char = s1[i]
            num_chars_missing += 1
            if char in chars_missing:
                chars_missing[char] += 1
            else:
                chars_missing[char] = 1

        for r in range(len(s2)):
            if r-l+1 > len(s1):
                old_char = s2[l]
                if old_char in chars_missing:
                    chars_missing[old_char] += 1
                    if chars_missing[old_char] > 0:
                        num_chars_missing += 1
                l += 1

            new_char = s2[r]
            if new_char in chars_missing:
                if chars_missing[new_char] > 0:
                    num_chars_missing -= 1
                chars_missing[new_char] -= 1

            if num_chars_missing == 0:
                return True

        return False


# Runtime: where n1 is length of 1, n2 is length of s2
# Create dict: O(n1)
# Loop over s2 O(n2). In each loop we do no looping just constant operations O(1)
# As n2 >= n1 ==> Overal runtime O(n1 + n2) which gets to O(n2)

# SpacE: O(n1) in the worst case if all chars are unique in s1
