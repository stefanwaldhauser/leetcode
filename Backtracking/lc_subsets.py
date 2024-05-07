from typing import List

# How many subsets are there?
# For each number in the list l we can decide to either include or not include in the subset
# That means if n is the total amount of elements in l, then the overall number of subsets is pow(2,n) IF we consider (2,3) and (3,2) different which we do not
# The longest subset has size n. for this longest subset we have to decide for each index if we include the number or not
# This means a natural worst case upper bound is O(n * pow(2,n))




# Backtracking solution
# Note: This is not "really backtracking, as we do not make a wrong choice here as all the numbers in the original nums are unique and we go through them in order"


# This is a classic way to think about this. Think about the problem like a decision tree and the ncode the decision tree
# Here we go through the list of nums and each node we decide to include the number in the or not in the set
# If you do this,you end up with the complete sets to include as the leaves of the decision tree
# One path will only be a NO in each decision so the empty set at the leaf
# One path will always be a YES in each decision so the full set at the leaf
# In the middle we will have a mix of them
def subsets_backtracking(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    #i is the index of the number we are making the decision for
    def dfs(i):
        if i >= len(nums): # Base Case: No more choices to make, reached a leaf node in the decision tree
            res.append(subset.copy())
            return

        # decision to include nums[i] (left decision)
        subset.append(nums[i])
        dfs(i+1)

        # decision not to include nums[i] (right decision)
        subset.pop()
        dfs(i + 1)
    dfs(0)
    return res

# https://stackoverflow.com/questions/69877504/time-complexity-for-all-subsets-using-backtracking
# Time Complexity: At the end we have 2^n leaf nodes, different subsets as for each of the n numbers we include or not include. Each build is O(n)
# as we have to go through the whole nums and make a decision for each. So the overall runtime is O(n * 2^n)



# As l only contains unique numbers, this solutions naturally leads to never generating (2,1) and (1,2) as the list l is trespassed in order
# Recursiive solution
def __subsets(l):
    if len(l) == 0: # base case as we exhausted all the options
        return [()]
    if len(l) == 1:
        return [(), (l[0],)] # Comma is needed to create a single element
    head, tail = l[0], l[1:]
    r = []
    l = __subsets(tail) # I trusy my recursion gives me a list of all the subsets for n-1 (the tail)
    for t in l: # I get the full result by simply adding the head to each of the subsets discovered
        r.append(t)
        r.append(t + (head,))
    return r


def subsets(nums: List[int]) -> List[List[int]]:
    result = __subsets(nums)
    return [list(t) for t in result] # Convert list of tuples to list of lists



# TEST CODE

print(subsets_backtracking([1,2,3]))
