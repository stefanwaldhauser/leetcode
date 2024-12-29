class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    solution = a + b
                elif token == '-':
                    solution = a - b
                elif token == '*':
                    solution = a * b
                else:
                    #  Python's floor division // always rounds toward negative infinity, not toward zero!
                    # To achieve divison towards 0 we have to do int() to just cut off the comma part
                    solution = int(a / b)
                print(f'{a} {token} {b} = {solution}')
                stack.append(solution)
            else:
                stack.append(int(token))
        return stack.pop()

# Runtime: O(n)
# Space: O(n)
