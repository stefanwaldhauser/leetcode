class Solution:
    def trap(self, height):
        n = len(height)
        traps = []
        if n < 3:
            return traps

        i = 0
        while i <= n - 3:  # Trap can not start with at least two indexes free space to the right
            # Trap cann ot start where there is nothing
            if height[i] < 1:
                i += 1
                continue
            j = i + 1
            # If directly after a wall comes another wall that is as big, there is nothing to trap
            if height[j] >= height[i]:
                i += 1
                continue
            # We now have at least have the possibility to trap water
            # We will look for the first wall that is at least as high as i which allows us to trap water between them
            while j < n and height[j] < height[i]:
                j += 1
            if j < n:
                traps.append([i, j])
            i = j
        return traps


print((Solution()).trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
