# Range [1,... n]. So if n = 4, [1,2,3,4].
# Note: Range means no duplicates
# 1 <= n <= 20
# 1 <= k <= n
# Given all combinations of k numbers from that range (ordering does not matter, drawing from a bag)

# The trick to prevent [1,2] and [2,1] from showing up is to offer not the whole list at once
# but at each level only offer to take the number or not.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solutions = []

        def backtrack(combination, offered_number):
            if len(combination) == k:
                solutions.append(combination.copy())
                return
            if offered_number > n:
                return
            # choice a) take offered number
            combination.append(offered_number)
            backtrack(combination, offered_number + 1)
            combination.pop()
            # choice b)do not take offered number
            backtrack(combination, offered_number + 1)

        backtrack([], 1)

        return solutions

# Another cool solution: We iterate over all choices but only those larger than the parent node,
# so we will only get [1,2] and not [2,1]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solutions = []

        combination = []
        def backtrack(start):
            if len(combination) == k:
                solutions.append(combination[:])
                return

            # Small optimisation: its possible that we do not have enough larger numbers left to fill
            need = k - len(combination)
            remain = n - start + 1
            available = remain - need


            # The trick is to start here from the parent, so all children are larger
            # Imagine n = 4
            # The child nodes of 1 are, 2,3,4
            # The child noes of 2, are 3,4
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1)
                combination.pop()

        backtrack(1)
        return solutions
