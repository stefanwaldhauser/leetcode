# https://leetcode.com/problems/valid-anagram/description/
from typing import List


# Note:
# Time : O(s + t) where s is the length of s and t is the length of t
# Space: O(s) where n is the length of s

# Neetcode Solution
def isAnagramTwo(s:str, t:str) -> bool:
    if len(s) != len(t) :
        return False

    countS, countT = {}, {}

    # We know they are the same length
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0) # Trick: Get function returns 0 if key is not there saving us the if else
        countT[t[i]] = 1 + countT.get(t[i],0)
    for c in countS:
        if countS[c] != countT.get(c, 0): # Trick: If the letter c does not exist in t we will return a 0 with the get. c definitely exists in s, so at least a 1, so this will fail
            return False
    return True

# Note:
# Time : O(s + t) where s is the length of s and t is the length of t
# Space: O(s + t) where n is the length of s and t is the length of t
