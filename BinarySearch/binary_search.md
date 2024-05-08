https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems


Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ASCENDING order. For most tasks, we can transform the requirement into the following generalized form:

MINIMIZE k , s.t. condition(k) is True

```
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left = min(search_space)
    right = max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right: # Search Space Not Yet collapsed to one element
        searchSpaceMid = left + (right - left) // 2 # right halve in odd case one element bigger
        if condition(searchSpaceMid): # mid is a FEASIBLE solution but not necessarily the minimal. DO NOT EXCLUDE from search space. Best one we have seen so far
            right = searchSpaceMid # Right is always the best one (smallest) we have seen so far in our minimize problem
        else:
            left = searchSpaceMid + 1 # mid is NOT a feasible solution. EXCLUDE
     # This loops stops when left == right which happens when the search space is narrowed down to one element, the minimal k satisfying the condition!
     return left
```

What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

- Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;

- Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;

- Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

The above problems are quite easy to solve, because they already give us the array to be searched. We'd know that we should use binary search to solve them at first glance. However, more often are the situations where the search space and search target are not so readily available. Sometimes we won't even realize that the problem should be solved with binary search -- we might just turn to dynamic programming or DFS and get stuck for a very long time.

As for the question "When can we use binary search?", my answer is that, !If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.! 
