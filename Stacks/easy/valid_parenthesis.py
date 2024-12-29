from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:  # closing
                if not stack:
                    return False
                top = stack.pop()
                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False
        return len(stack) == 0

# Runtime: O(n)
# Space: O(n)
