class Solution:
    # Basically the trick here is that we have to rephrase the choice
    # Instead of: the choice is this array of numbers (with duplices)
    # It is: the choice is how much of each unique numbers
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1

        def backtrack(solution, num_count):
            if len(solution) == len(nums):
                solutions.append(solution.copy())
                return

            for num in num_count.keys():
                if num_count[num] > 0 :
                    solution.append(num)
                    num_count[num] -= 1
                    backtrack(solution, num_count)
                    num_count[num] += 1
                    solution.pop()
        backtrack([], num_count)
        return solutions
