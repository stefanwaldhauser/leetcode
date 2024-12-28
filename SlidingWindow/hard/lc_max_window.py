import collections
from heapq import heapify, heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        result = []

        h = []

        l = 0
        for r in range(len(nums)):
            heappush(h, (-nums[r], r))
            if r < k-1:
                continue
            while h[0][1] not in range(l, r+1):
                heappop(h)
            result.append(-h[0][0])
            l += 1
        return result


# Time Complexity: O(n log n)
# - Where n is the length of the input array nums

# Here's the breakdown:
# - The main loop runs n times (iterating through nums)
# - In each iteration:
# - heappush operation takes O(log n) time
# - The while loop with heappop operations in worst case might need to remove multiple elements, but each element is pushed and popped exactly once throughout the entire algorithm
# - The range check is O(1)

# Even though we might have multiple pops in one iteration, !!!across the entire execution!!!!:

#     Each element is pushed exactly once: n * O(log n)
#     Each element is popped at MOST once: n * O(log n)


# Space Complexity: O(n)
# - The heap h in worst case might store all elements of the array

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0

        # increasing indices q[0] is smallest index, q[-1] is largest index
        # decreasing values nums[q[0]] is largest value, nums[q[-1]] is smallest value

        # nums[q[0]] should represent the max for our window, nums[q[i]] in general are potential max for future window
        q = collections.deque()  # indices

        while r < len(nums):
            # nums[r] is of course a new potential max for the current and future windows
            # but by adding it we can definitely eliminate previous possibilities
            # as a smaller value can now never be maximum again
            # by popping from the right to the left it guarantees a decreasing order. and if it is the new maximum
            # it will then be on q[0] as everythin else would have been popped
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # the smallest index is on the left, this could now be outside of the window or NOT
            # because of the popping from above its possible that it is still in the window
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        return output

# Runtime: O(n)
# This is why the solution is efficient - despite having a while loop inside another while loop, each element is processed at most twice (push and pop), giving linear time complexity.
# Space: O(n)
