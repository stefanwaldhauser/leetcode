from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        # mins stores current and previous mins (strictly increasing)
        # mins[0] is the current min
        # If you build a stack:
        # - you find a number that is larger than the current min, you do not have to do anything as it will never be the min of the stack (it will be popped before the current min)
        # - you find a number that is smaller or equal to the current min, this will now become the current min ! as long as it is not popped ! so we append it left
        self.mins = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[0]:  # new overall min
            self.mins.appendleft(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if self.mins and val == self.mins[0]:
            self.mins.popleft()  # current min is gone, next one will become min

    def top(self) -> int | None:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int | None:
        return self.mins[0] if self.mins else None


# Alternative approaches could include:
# 1. Storing(value, current_min) pairs in the main stack - O(n) space but simpler code
# 2. Recalculating min on each getMin call - O(1) space but O(n) time for getMin
# 3. Using a sorted set for mins - more complex but potentially better space in some cases

class MinStackAlternative:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # If stack is empty, val is the current minimum
        if not self.stack:
            self.stack.append((val, val))
        else:
            # New minimum is either the new val or the previous minimum
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int | None:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int | None:
        return self.stack[-1][1] if self.stack else None
