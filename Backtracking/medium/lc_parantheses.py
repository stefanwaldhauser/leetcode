# https://leetcode.com/problems/generate-parentheses/



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        PAIRS = n
        LENGTH = 2 * n # always even
        all_paranthesis = []
        def backtrack(paranthesis, no_open, no_closed):
            # Prune the branch in the decision tree if we reached a bad state
            # Bad State: Added one to many closed brackets (can never recover from it)
            if no_closed > no_open:
                return
            # bad State: Added more than PAIRS brackets of one type
            if no_open > PAIRS:
                return

            if len(paranthesis) == LENGTH:
                all_paranthesis.append(paranthesis.copy())
                return
            # choice a -> Add (
            paranthesis.append("(")
            backtrack(paranthesis, no_open + 1, no_closed)
            paranthesis.pop() # revert decision

            # choice b -> Add )
            paranthesis.append(")")
            backtrack(paranthesis, no_open, no_closed+1)
            paranthesis.pop() # revert decision

        backtrack([], 0, 0)

        result = [''.join(sublist) for sublist in all_paranthesis]

        return result
