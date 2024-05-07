https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63d3bcd7f81b8e2fe5ded81c
 - In backtracking, we build a solution incrementally and follow the approach that if the current solution can’t lead to a valid solution, abandon it and backtrack (or go back) to try another solution. Because of this, recursion becomes a suitable technique for solving backtracking problems.# - Dynamic Programming (DP) uses a similar approach where we try out all possible solutions (using Memoization) to pick up the most optimized solution. backtracking, on the other hand, is mostly used when multiple valid solutions are possible for a problem. backtracking, on the other hand, is mostly used when multiple valid solutions are possible for a problem. This approach of evaluating all possible solutions, going back whenever we see that a certain constraint can’t be met, and trying out other possible solutions is called backtracking.


# ChatGPT
The backtracking pattern is a systematic way to iterate through all the possible configurations of a given problem space to find solutions to a computational problem. It is a depth-first search (DFS) approach for solving constraint satisfaction problems such as puzzles, combinatorial problems, and pathfinding in graphs.

Backtracking works by exploring potential solutions incrementally, abandoning each partial solution ("backtracking") as soon as it determines that this partial solution cannot possibly lead to a viable complete solution. The key idea is to make a choice at each step, proceed forward to see if this choice leads to a solution, and if not, undo the choice (backtrack) and try another option.

-> You basically go as deep as you go until you violate a constraint, then undo one step and try another option and rpeeast

# Key Features of Backtracking:
Choice: At each step, you have a set of choices. You choose one and move to the next step.
Constraints: Rules that must be followed for a solution to be considered valid. If a choice violates a constraint, it is abandoned.
Goal: The condition that must be met to consider a problem solved.

# Steps in Backtracking Algorithm:
Choose: Choose the next option to move forward with. If there are no more options to try or if a certain threshold is reached, backtrack.
->
Constrain: Check if the current choice violates any constraints. If it does, abandon this choice (backtrack) and try another.
->
Goal: Check if the current solution satisfies the goal. If so, record the solution or return it.

# Example Problems Solved Using Backtracking:
Permutations and Combinations: Generating all possible arrangements or selections of a set of items.
Sudoku Solver: Filling a Sudoku puzzle by placing numbers according to the rules.
N-Queens Problem: Placing N chess queens on an N×N chessboard so that no two queens threaten each other.
Subset Sum Problem: Finding a subset of numbers that sum up to a given number.
Path Finding Problems: Finding paths in a grid or graph that satisfy certain conditions.

# How is it related to recursion?

Backtracking algorithms typically use recursion to explore the decision tree of all possible paths. The structure of a backtracking function might look like this in pseudocode:

```
function backtrack(path, choices):
    if path is a solution:
        add path to solutions
        return # Go back one step as we found a valid solution

    for choice in choices: # Explore all valid choices by a series of recursive calls
        if choice is valid:
            make choice # possible performign any changes
            backtrack(path + [choice], choices) # Go one level deeper with the result of the choice
            undo choice # possibly undoing any change
            return
        return # Not a valid chocie
    return # No more choices
```

# Why Use Backtracking?
Backtracking is used because it offers a structured way to iterate over all possible configurations of a problem. While not always the most efficient (some problems might require optimization techniques to reduce the search space), it ensures that all potential solutions are considered. It's particularly useful in situations where the problem domain is discrete and finite, and where brute-force enumeration is impractical due to the combinatorial explosion of possibilities.

-> Sometimes the search space is so vast that a pure brute force solution will not work therefore we need to do a "smart" brute force

# Detailed Relationship to Recursion
Relationship to Recursion
Recursive Framework: Backtracking utilizes a recursive method to explore all the potential solutions of the problem. Each recursive call represents a decision point where multiple options or paths might be pursued.

Base Case: In recursion, a base case defines the condition under which the recursion stops. ** In backtracking, the base case often checks if the current candidate forms a complete solution to the problem. If so, the solution is usually recorded, and the recursion ends for that path. **

Recursive Case: This involves continuing to build on a partial solution. In backtracking, if the current state of the solution does not violate problem constraints, the algorithm explores further by making a series of recursive calls, each representing a different choice that extends the current solution.

Backtracking Step: This is where the algorithm diverges from simple recursion. In backtracking, if it's determined that the current partial solution cannot possibly lead to a valid final solution (either because it already violates the constraints or there are no more options to extend it), the algorithm "backs up" by undoing the last step and tries another path. This involves returning from the recursive call and possibly undoing any changes made by that call, hence "backtracking" to explore different options.
