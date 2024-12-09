class Solution:
    def trap(self, height):
        n = len(height)
        trapped_rain = 0
        if n < 3:
            return trapped_rain

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
                walls_in_between = 0
                for k in range(i+1, j):
                    walls_in_between += height[k]
                trapped_rain += ((j-i-1) *
                                 min([height[i], height[j]]) - walls_in_between)
                i = j
            # There is no right wall
            else:
                i += 1
        return trapped_rain
