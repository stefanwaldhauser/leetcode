# https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 1:
            return 1 / x *  (self.myPow(x, n +1))
        return x * self.myPow(x, n-1)

# Works but really expensive as the maximum recursion depth explodes

# Time Complexity: O(N) as we have a recursion tree of N nodes and we visit each one of them and perform O(1)
# Space Complexity: O(N) as we have the recursion tree of N level


#  By repeatedly squaring x and halving n, we can quickly compute x^n using a logarithmic number of multiplications.
#  If n is even, we can say that x^n = (x^2)^(n/2) (Example x^6 = (x^2)^(6/2) = (x^2)^3
#  If n is odd, we just have to extract one x to make it even, and then use above formulas
#  x^n = x * x^(n-1) = x * (x^2)^((n-1)/2)


# With this trick instead of reducing n by 1 each recursive call, we can half it each step
# 2 ^ 100 = (2^2)^50 = 4^50 (level 0) (n halfed)
# 4 ^ 50 = (4^2)^25 = 16^25 (level 1) (n halfed)
# 16 ^ 25 =ODD= 16 * 16 ^ 24 = 16 & (16^2)^12 (n halfed)
# ....



class BinaryExponentationSolution:
    def myPow(self, x: float, n: int) -> float:
        def _myPow(x, n_abs):
            if n_abs == 0:
                return 1
            if n_abs == 1:
                return x
            if n_abs % 2 == 0: # even
                return _myPow(x*x, n_abs//2)
            return x * _myPow(x*x, (n_abs-1)//2) # odd
        res = _myPow(x, abs(n))
        if n < 0:
            return 1/res
        return res

# Time Complexity: O(log2(n)) as we half each step n
# Space Complexity: O(log2(n)) as we have the recursion tree of log2(n)
