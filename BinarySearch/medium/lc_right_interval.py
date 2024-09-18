# https://leetcode.com/problems/find-right-interval/description/?envType=study-plan-v2&envId=binary-search
from typing import List
# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.
# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

# Praktisch: In der liste der intervall muss mann wenn moglich zu jedem interval das minimale andere interval finden\
# dass rechts anschliesst. Also das dort anfängt wo das andere aufhort

# Problem Breakdown:

# You are given an array of intervals. Each interval consists of a start time and an end time.
# For each interval, you want to find the "right" interval. The "right" interval is the next interval(from the list) that starts after or at the same time as the current interval ends, and it must have the smallest start time possible.
# If no such interval exists, return -1 for that interval.

# Real-World Example:

# Imagine you are organizing meetings, and each interval represents a meeting. You want to find the next available meeting that starts after or at the same time your current meeting ends. If no such meeting exists, you note down - 1.


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_index_to_original_position = {}
        solutions = [-1] * len(intervals)

        # as the start index is unique we can store the original position in a dict
        for i, interval in enumerate(intervals):
            start_index_to_original_position[interval[0]] = i

        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])


        for interval in sorted_intervals:
            l = 0
            r = len(sorted_intervals)

            while l < r:
                mid = l + (r-l) // 2
                mid_interval = sorted_intervals[mid]

                is_right_interval = mid_interval[0] >= interval[1]
                if is_right_interval:
                    r = mid
                else:
                    l = mid + 1
            if l != len(sorted_intervals):
                solutions[start_index_to_original_position[interval[0]]] = start_index_to_original_position[sorted_intervals[l][0]]

        return solutions

# Sorting O(log N)
# Then we run N * O(logN) binary searches
# Overall: O(N * logN)
