from typing import List
# https://leetcode.com/problems/combination-sum/

# The trick is to formulate the decisio n tree such that no duplicates are possible.
# Imagine the scenario [2,3,6,7]
# Imagine the root. And one choice is that you MUST include at least one ADDITIONAL 2 and the other choice is that you can NOT ANY ADDITIONAL 2, but instead use something form the other numbers
# This means the combinations are guarenteed to be duplicate free
# If we follow an edge we can either say: include one additional number or exclude this number from ever being added again
# This can be tracked with an i pointer. The pointer says

# Time Complixity: As the numbers are positive, at least 1. The maximum of the tree is therefore limited to Target.
# Its a binary decision tree, so the number of nodes is O(2^Target)


# Neetcode solution:
# https://www.youtube.com/watch?v=GBKI9VSKdGg
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def _combination_sum(i, cur, total):
        if total == target: # Base Case Succeed
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target: # Base Case Fail
            return

        # Decision A: Include another candidates[i]
        cur.append(candidates[i])
        _combination_sum(i, cur, total + candidates[i])
        cur.pop()
        # Decision B: Stop including another candidates[i]. Dont make a coice for anyhting else yet, just do not include candidatespi
        _combination_sum(i+1, cur, total)

    _combination_sum(0, [], 0)
    return res


# Leetcode Premium Solution

# The trick they do is that you make a decision for an index in candidates. This choice means that you explore from that
# index until the end. From that index as you can include on number multiple times. Imagine candidates [3,4,5].
# Basically: The decision is: Add candidate i and restrict furher choices form [i, end]. The candidate list is unique, this menas
#     (LEFT_SIBLING) (NODEX) (RIGHT-SIBLING)
# if NodeX has coices [i:] the left sibling deals with [i-1,:] and the right sibling [i+1,:]


# Decision 0: [3], i = 0
# Decision 1: [4], i = 1
# Decision 2: [5]  i = 2


# Ordering is not important! Do not return [2,3] and [3,2]. It needs to be unique combinatons
# each candidate can be used as many times as you want
# candidates 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# all elements of candidates are distinct
# 1 <= target <= 40


class Solution:
    def combinationSum(this,candidates: List[int], target: int) -> List[List[int]]:
        solutions = []


        def backtrack(solution, solution_sum, candidate_i):
            if solution_sum == target:
                solutions.append(solution.copy())
                return
            if solution_sum > target:
                return
            if candidate_i > len(candidates) - 1:
                return

            # choose candidate
            candidate = candidates[candidate_i]
            solution.append(candidate)
            # Leave it in the list of candidates as we can choose again
            backtrack(solution, solution_sum + candidate, candidate_i)
            solution.pop()
            # do not choose candidate and remvoe it form the list
            backtrack(solution, solution_sum, candidate_i + 1)


        backtrack([], 0, 0)
        return solutions
