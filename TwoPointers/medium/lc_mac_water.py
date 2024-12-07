class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        l = 0
        r = len(heights) - 1

        max_a = 0

        # This is an optimization problem. Each time we move any of the two pointer x gets smaller, so all depends on the height
        # If we would move the larger bar, we would definitely get worse asthe limiting factor is the smaller bar
        # Therefor the only wait to potentially improve is to always move the smaller of the two bars
        while l < r:
            x = r - l
            h = min([heights[l], heights[r]])
            a = x * h
            if a > max_a:
                max_a = a
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_a

# Runtime: O(n)
# Space: O(1)
