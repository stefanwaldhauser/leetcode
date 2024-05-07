# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    # Basically this is just fibonacci
    # F(N) = F(N-1) + F(N+2)
    def climbStairs(self, n: int) -> int:
        cache = {0:1, 1:1}
        def _climb_stairs(n):
            if n in cache:
                return cache[n]
            cache[n] = _climb_stairs(n-1) + _climb_stairs(n-2)
            return cache[n]
        return _climb_stairs(n)
