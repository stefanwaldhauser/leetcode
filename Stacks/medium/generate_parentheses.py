class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        current_stack = []
        def backtrack(open_count, current):
            if len(current) == n * 2:
                if len(current_stack) == 0:
                    solutions.append(''.join(current))
                return

            # option 1: add open bracket
            if open_count < n:
                current_stack.append('(')
                backtrack(open_count+1, current + '(')
                current_stack.pop()

            # option 2: add closing bracket
            if len(current_stack) > 0 and current_stack[-1] == '(':
                current_stack.pop()
                backtrack(open_count, current + ')')
                current_stack.append('(')

        backtrack(0, '')

        return solutions


# Can be done without stack:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count: int, close_count: int, current: str):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(open_count + 1, close_count, current + '(')

            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ')')

        result = []
        backtrack(0, 0, '')
        return result
