from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: count each number
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1

        # step 2: invert, so store for each count which numbers have that count
        freq_to_nums = defaultdict(list)
        for num, freq in num_to_freq.items():
            freq_to_nums[freq].append(num)

        # Step 3: Maximum count is n, try to go one by one until you found k numbers
        n = len(nums)

        solution = []
        for i in range(n, -1, -1):
            if i in freq_to_nums:
                for num in freq_to_nums[i]:
                    if len(solution) < k:
                        solution.append(num)
        return solution


# Runtime: Step 1, 2, 3 are O(n). O(3n) == O(n)
# Space: two dicts and an array each O(n). O(3n) == O(n)


class HeapSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1

        heap = []
        for num, freq in num_to_freq.items():
            heap.append((-freq, num))
        heapify(heap)

        solution = []
        for _ in range(k):
            solution.append(heappop(heap)[1])
        return solution

#     First loop to build frequency map:
#     - Iterates through nums array once
#     - Dictionary operations are O(1)
#     - Time: O(n) where n is length of nums

#     Building heap array and heapification:
#     - Iterates through unique numbers in num_to_freq
#     - heapify operation is O(m) where m is number of unique elements
#     - Time: O(m) where m is number of unique elements

#     Final loop for extracting k elements:
#     - Performs k heappop operations
#     - Each heappop is O(log m)
#     - Time: O(k log m)


# Total Runtime: O(n + m + k log m) where:
# - n is length of input array
# - m is number of unique elements
# - k is given parameter

# Since m ≤ n(number of unique elements can't exceed array length), we can simplify to:
# O(n + k log n)

# Space Complexity:
# - Dictionary: O(m)
# - Heap: O(m)
# - Solution array: O(k)
# Total Space: O(m) or O(n) in worst case


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = defaultdict(int)

        # For each possible count (0, n) we create a list of those elements with that count
        freq = [[] for _ in range(n + 1)]

        for num in nums:
            count[num] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(n, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Runtime: O(n)
# Space: O(n)
