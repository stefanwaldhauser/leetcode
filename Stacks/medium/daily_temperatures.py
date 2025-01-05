class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []

        # Monotonic decreasing stack approach
        # - The code iterates from right to left through the temperatures array
        # - This is because it means we've already processed all future days when looking at any current day
        # - The loop removes any temperatures from the stack that are less than or equal to the current temperature
        # - Why? Because if we find a future day that's colder or equal, it can never be the answer for any previous day (as we already have a warmer or equal day closer)
        # If the stack isn't empty after removing smaller/equal temperatures, the top of stack contains the next warmer day

        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack:
                solution[i] = stack[-1][0] - i
            stack.append([i, temperatures[i]])

        return solution

# Runtime: O(n)
# Space: O(n)


# The Stack's Purpose
# - The stack keeps track of indices of temperatures that haven't found their "next warmer day" yet
# - These temperatures are stored in decreasing order (from top to bottom)
# - We only store indices in the stack, not the actual temperatures

# There is also a forward iteraton approach
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        solution = [0] * n
        stack = []

        for i in range(n):
            # We check if it's warmer than any temperatures waiting in our stack
            # if it is warmer, we've found the "next warmer day" for those waiting temperatures
            # If a temperature is warmer than what's in the stack, it must be the next warmer temperature for those days
            # We can't find a closer warmer day because we're going through the days in order
            # The stack naturally maintains temperatures in decreasing order because we remove any temperatures that are colder than what we're currently processing
            # The beauty of this solution is that it mimics how we might solve this problem in real life: keep a list of "waiting" temperatures and cross them off when we find their next warmer day.
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_idx = stack.pop()
                solution[prev_idx] = i - prev_idx
            stack.append(i)

        return solution


class AnotherSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # what we want is the next larger temperature, we use a continous stack for this
        solution = [None] * len(temperatures)

        stack = []
        for i in range(len(temperatures)):
            # i is the index of the next larger temperature for the elements in the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                solution[popped] = (i-popped)
            # Just as a note
            # We popped all smaller or equal temperatures
            # Stack[-2] is the previous larger temperature for stack[-1] and so on, therefore monotonic stack
            stack.append(i)

        while stack:
            popped = stack.pop()
            solution[popped] = 0

        return solution
