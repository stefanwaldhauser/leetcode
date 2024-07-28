from collections import defaultdict
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []

        # Count occurrences of each candidate
        candidate_count = defaultdict(int)
        for candidate in candidates:
            candidate_count[candidate] += 1

        # Sort unique candidates for optimization
        unique_candidates = sorted(candidate_count.keys())

        solutions = []

        def backtrack(start: int, curr_solution: List[int], remaining: int):
            if remaining == 0:
                solutions.append(curr_solution[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(unique_candidates)):
                candidate = unique_candidates[i]
                if candidate > remaining:
                    break  # Optimization: no need to check larger candidates

                if candidate_count[candidate] > 0:
                    curr_solution.append(candidate)
                    candidate_count[candidate] -= 1

                    backtrack(i, curr_solution, remaining - candidate)

                    curr_solution.pop()
                    candidate_count[candidate] += 1

        backtrack(0, [], target)
        return solutions
