# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq
from typing import List


# Main trick here: The smallest element in a list of size k is automatically the k largest (namely the largest overall), or
# the largest element in a list of size k is automatically the k smallest (namely the smallest overall)
# So to find the k largest just build and maintain a MIN heap of size k
# So to find the k smallest just build and maintain a MAX heap of size k


# Note: In out dummy heap building the heap toke O(n log n) but there are better algorithms that can do it in O(n)
# For the runtime analysis we use O(n) here
class KthLargest:


    def __init__(self, k: int, nums: List[int]): #O(len(nums) + (len(nums) - k))
        self.k = k
        self.k_min_heap = nums.copy() # Build the initial heap
        heapq.heapify(self.k_min_heap) # Building the initial heap takes
        # Pop off elements until only k elements are on the min heap,
        # In a list of say 3 elements, the smallest is by definition the 3rd largest, thats we trick we use here
        while len(self.k_min_heap) > k:
            heapq.heappop(self.k_min_heap) #
        # We now have a min heap of size k, this means the top element is the kth largest

    def add(self, val: int) -> int:
        heapq.heappush(self.k_min_heap, val)
        if(len(self.k_min_heap) > self.k):
            heapq.heappop(self.k_min_heap) # Only pop if we have more than k elements
        return self.k_min_heap[0]
