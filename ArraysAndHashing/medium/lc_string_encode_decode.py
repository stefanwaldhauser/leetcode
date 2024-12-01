from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        str_lengths = []
        for s in strs:
            str_lengths.append(str(len(s)))
        prefix = "[" + ",".join(str_lengths) + "]"
        return prefix + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 2:
            return []
        encoded_start = s.index("]") + 1
        prefix = s[1:encoded_start-1]
        str_lengths = prefix.split(",")

        solution = []

        start = encoded_start
        for l in str_lengths:
            solution.append(s[start:(start+int(l))])
            start = start + int(l)

        return solution

# Another solution is to encode the length as symbol '<length>#' for each word in the string. # is needed as a word could start with a number
class AnotherSolution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # j is now at pound sign, [i,j) is the length of the word after the pound sign
            length = int(s[i:j])
            i = j + 1 # first char after pound sign
            j = i + length #first char of the next length
            res.append(s[i:j])
            i = j

        return res
