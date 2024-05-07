class Solution:
    # Basically this is just fibonacci
    # F(N) = F(N-1) + F(N+2)
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Runtime: O(n)
# Space: O(n)
