
# Runtime: m is amount of strings and n is the lenght of the longeststring
# Runtime: O(m * O(n*log(n)))
# Space: O(m)


class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_str = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in sorted_to_str:
                sorted_to_str[sorted_str].append(str)
            else:
                sorted_to_str[sorted_str] = [str]
        return sorted_to_str.values()


# Instead of sorting O(n * log(n)) we crate a character count hash that only takes O(n)
# So Runtime becomes O(m + n)
class BetterSolution:
    def characterCountTupel(self, s):
        char_count = [0] * 52  # 26 upper case, 26 lower case
        for c in s:
            # upper
            if c.isupper():
                # upper case get mapped from 26 onwards, right where we left of with the lower case
                index = ord(c) - ord('A') + 26
            else:  # lower
                # a (26) gets mapped to 0, b(27) gets mapped to 1, z(51) gets mapped to 25
                index = ord(c) - ord('a')
            char_count[index] += 1
        return tuple(char_count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            char_count = self.characterCountTupel(s)
            if char_count in d:
                d[char_count].append(s)
            else:
                d[char_count] = [s]
        return d.values()
