# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
import math
from typing import List



def euclidian(p, q):
    [px,py],[qx,qy] = p,q
    return math.pow((px-qx),2)+math.pow(py-qy) # Dont even need the sqrt

# To find th kth smallest object use a max heap of size k
# <---> use a min heap of size k IF you negate all comparison value
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    h = []
    heapq.heapify(h)
    for p in points:
        distance = -1 * euclidian(p, [0,0]) # negate the values so we can use a minHeap instead of a maxHeap
        heapq.heappush(h, [distance, p])
    while(len(h) > k):
        heapq.heappop(h)
    return list(map(lambda x: x[1], h)

# Runtime: Each insertion takes O(log n) so we have n points so it takes O(n log n)

# We also could have used a min heap of cours, build the whole heap and then pop k times

### TESTCODE

print(k_closest([[3,3],[5,-1],[-2,4]], 2))
