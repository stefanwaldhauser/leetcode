from collections import defaultdict
from typing import List

# This is a version where the decision is non-binary. At each step we try the
class Solution:
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            if not candidates or target <= 0:
                return []

            candidate_count = defaultdict(int)
            for candidate in candidates:
                candidate_count[candidate] += 1

            unique_candidates = sorted(candidate_count.keys())

            solutions = []

            # The start parameter determines the starting index in the unique candidates
            # from which we begin considering candidates for the current combination

            def backtrack(start: int, curr_solution: List[int], remaining: int):
                # Positive Base Case: We have found a valid solution
                if remaining == 0:
                    solutions.append(curr_solution.copy())
                    return

                # Negative Base Case: We overshot the target
                if remaining < 0:
                    return

                # The choice we make here is
                for i in range(start, len(unique_candidates)):
                    candidate = unique_candidates[i]
                    if candidate > remaining:
                        break  # Optimization: no need to check larger candidates

                    if candidate_count[candidate] > 0:
                        curr_solution.append(candidate)
                        candidate_count[candidate] -= 1
                        # keep index to you can reuse numbers
                        backtrack(i, curr_solution, remaining - candidate)

                        curr_solution.pop()
                        candidate_count[candidate] += 1

            backtrack(0, [], target)
            return solutions



# This is a version where the decision is binary. For each candidate we either include them in the solution or not
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []

        # Use a count of candidates instead of a list to solve the duplicate problem.
        candidate_count = defaultdict(int)
        for candidate in candidates:
            candidate_count[candidate] += 1
        # The sorting of candidates allows the algorithm to stop early when it encounters a number larger than the remaining target.
        unique_candidates = sorted(candidate_count.keys())

        solutions = []

        def backtrack(candidate_i: int, curr_solution: List[int], remaining: int):
            # Positive Base Case: We have found a valid solution
            if remaining == 0:
                solutions.append(curr_solution.copy())
                return
            # Negative Base Case: We overshot the target or we are out of candidates
            if remaining < 0 or candidate_i >= len(unique_candidates):
                return

            # Middle of the tree. For the current candidate we
            candidate = unique_candidates[candidate_i]
            # Pruning: The list of candidates is sorted. If candidate at i is already too big, all following will also be too big
            if candidate > remaining:
                return

            # Choice: Include the current candidate (can be only made if count is high enough)
            if candidate_count[candidate] > 0:
                curr_solution.append(candidate)
                candidate_count[candidate] -= 1
                # Important: We try the same candidate again. This guarantees we always use the candidates up fully in one path
                backtrack(candidate_i, curr_solution, remaining - candidate)
                curr_solution.pop()
                candidate_count[candidate] += 1
            else:
                # Choice: Do not include the candidate and skip it
                backtrack(candidate_i + 1, curr_solution, remaining)

        backtrack(0, [], target)
        return solutions
