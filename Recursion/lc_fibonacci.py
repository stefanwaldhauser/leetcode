# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        cache = {} # We could have stored the base case already here and do not need to do the check  | cache = {0: 0, 1: 1}
        def _fib(N): # Using memoization to prevent duplicated technology in recursion tree
            if N in cache:
                return cache[N]
            result = None
            if N == 0:
                result = 0
            elif N == 1:
                result = 1
            else:
                result = _fib(N-1) + _fib(N-2)
            cache[N] = result
            return result
        return _fib(N)

# Time Complexity O(N) (no repeated calculations so NOT O(2^N))
# Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.
# Space complexity: O(N).
# The size of the stack in memory is proportional to N. Also, the memoization hash table is used, which occupies O(N)O(N)O(N) space.

# Leetcode Solution
class LCSolution:
    cache = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.cache[N]
