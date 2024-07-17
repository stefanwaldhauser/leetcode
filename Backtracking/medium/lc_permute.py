#https://leetcode.com/problems/permutations/

# Note: 1 <= nums.length <= 6 so really small
# Perfect candiate for backtracking as recursion depth will be really small
# Also the cost for searching the current solution is negligible

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        def backtrack(solution):
            if len(solution) == len(nums):
                solutions.append(solution.copy())
                return

            for num in nums:
                if num not in solution: # Remember len(nums) <= 6 so this barely costs anything!
                    solution.append(num)
                    backtrack(solution)
                    solution.pop()
        backtrack([])
        return solutions
