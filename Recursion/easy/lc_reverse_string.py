from typing import List
# https://leetcode.com/problems/reverse-string/
# Reverse with extra memory
def reverse(s):
    if len(s) == 0:
        return s
    return s[-1:] + reverse(s[:-1])

# Usage
print("EXTRA MEMORY")
print(reverse(""))
print(reverse("a"))
print(reverse("abc"))


# Reverse in memory
# an in-place algorithm is an algorithm that transforms input using no auxiliary data structure.
# In-place for recursive solutions means:
#  not having additional space consumption between two consecutive recursive calls, i.e. we should divide the problem into independent subproblems.
# So one of the ideas about how to divide the problem would be reducing the input string at each step into two components:
# 1). the leading and trailing characters. 2). the remaining substring without the leading and trailing characters.
# We then can solve the two components independently from each other.

# Basically you need to find independeny subproblems that you do not have to combine to get the full solution
# You solve them independently in any order and then you get the full result

def reverse_in_memory(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    # Trick is the following:
    # Do a classic divide and conquer
    # Imagine you have [a,b,c,d] (reversed it needs to be pd,c,b,a])
    # What if you could reverse the inner (smaller, simpler) part in memory (so without head and tail)
    # Then all you need to do is swap the beginning and the end also in memory to
    # As we need to do everything in memory we need to usw two pointers

    def _recursion(left,right):
        if left >= right: # Done
            return
        # reverse "inner" part
        _recursion(left +1, right - 1)
        # swap outer parts
        s[left], s[right] = s[right], s[left]
    _recursion(0, len(s) - 1)

# Note: Why can we do the swap here without any additional temp variable:
# The code works because you are not modifying the two elements with two separate statements.
# You have basically extracted them as a tuple and assigned them the values ​​currently in memory,
# and the values ​​in memory are not changed until the entire instruction is processed correctly.



# Space Complexity:
    # We perform N/2 recursive call so O(N) to keep the recursion stack until it collapeses
    # CAREFUL: RECURSION IS NOT CONSTANT SPACE, BECAUSE WE HAVE TO KEEP THE RECURSIVE STACK
# Time Complexity:
    # We perform N/2 swaps so O(N)





print("IN MEMORY")
a = ["a", "b", "c"]
reverse_in_memory(a)
print(a)
