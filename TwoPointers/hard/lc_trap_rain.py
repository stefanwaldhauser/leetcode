class Solution:
    def trap(self, height):
        n = len(height)
        n = len(height)
        trapped_rain = 0
        if n < 3:
            return trapped_rain

        prefix_sum = [0] * len(height)
        current_sum = 0
        for i in range(n):
            current_sum += height[i]
            prefix_sum[i] = current_sum

        i = 0
        while i < n:
            if height[i] == 0:
                i += 1
                continue
            # left wall found at index i -> search for right wall at index j
            j = -1

            k = i + 1
            while k < n:
                if height[k] > 0:
                    # if we find an equal or larger wall it is definitely the right wall
                    if height[k] >= height[i]:
                        j = k
                        break
                    # we store the largest of all walls. If there is no equal or larger wall, this will our right wall
                    if j == -1 or height[k] > height[j]:
                        j = k
                k += 1

            # We found a right wall
            if j != -1:
                walls_in_between = prefix_sum[j-1] - prefix_sum[i]
                trapped_rain += ((j-i-1) *
                                 min([height[i], height[j]]) - walls_in_between)
                i = j
            # There is no right wall
            else:
                i += 1
        return trapped_rain

# Runtime: O(n^2) # To get rid of it in the worst case we need to get rid of the nested loop structure
# Space: O(1)


class BetterSolution:
    def trap(self, height):
        max_height_to_the_left, max_height_to_the_right = [
            0] * len(height), [0] * len(height)

        max_height_left_seen = 0
        for i in range(0, len(height)):
            max_height_to_the_left[i] = max_height_left_seen
            max_height_left_seen = max([max_height_left_seen, height[i]])

        max_height_right_seen = 0
        for i in range(len(height)-1, -1, -1):
            max_height_to_the_right[i] = max_height_right_seen
            max_height_right_seen = max([max_height_right_seen, height[i]])

        trapped = 0

        for i in range(0, len(height)):
            possible_trapped = min(
                [max_height_to_the_left[i], max_height_to_the_right[i]])
            actually_trapped = max([0, possible_trapped - height[i]])
            trapped += actually_trapped

        return trapped

# To decide how much water is trapped above each cell, we need to just look at the largest walls to the left and to the right of the cell
# The smaller of those two is the possible water we can trap above the cell.
# The actual water is the possible water - the height at that cell. If larger 0 water can be trapped

# Runtime: O(n)
# Space: O(n)


class BestSolution:
    def trap(self, height):
        l, r = 0, len(height)-1
        max_l, max_r = height[l], height[r]

        trapped = 0
        while l < r:
            # The max_l is always the 'real' full max_l for the left pointer
            # The max_r is always the 'real' full max_r for the right pointer

            # We know the maximum height to the left of position l (that's our max_l)
            # We know there exists at least one wall of height max_r to the right (our current max_r)
            # Even if there are smaller values between l and r
            #  Any smaller values between l and r are irrelevant because:
            # - They can't increase the maximum possible water level (already limited by max_l)
            # - They can't decrease it because the water is "trapped" between max_l and the higher max_r
            if max_l < max_r:
                # first position never traps water so we can increment immediately
                l += 1
                max_l = max([max_l, height[l]])
                trapped += max_l - height[l]
            else:
                # last position never traps water so we can decrement immediately
                r -= 1
                max_r = max([max_r, height[r]])
                trapped += max_r - height[r]

        return trapped
