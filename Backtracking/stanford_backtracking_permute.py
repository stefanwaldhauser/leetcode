# https://www.youtube.com/watch?v=lr72sVlXFAw

# Schema:
# explore (decisions):
#   if there are no more decisions to make: stop (here often we do an extra step like only add to result if a specific constraint is meant like it does not contain it lready)
#   else, this call will make a single decision for each available choice C that we could make: (often with a foor loop)
#       ChooseC
#       Explore the remaining decisions (Recursive call most of the time!
#       Unchoose C (so another of the avilable choices can be made)


# Goal: Find all permutations, meaning orderings of the letter in a string
# Example: permute ("MARTY")
# We have 5 positions for each of those we must decide which letter to put there

def permute(s):
    res = []
    choice = []
    letters = list(s) # List of letter we can choose from

    def _permut():
        if(len(choice) == len(s)):
            res.append("".join(choice)) # If we did not want ot have any duplicats in it because s contains multiple the same letters, we would have to check if res already contains it and only then add it
            return
        for i in range(len(letters)): # Basically do a DFS down all edges from this current decision node
            letter = letters[i]
            # Choose C
            choice.append(letter)
            letters.pop(i)
            # Explore
            _permut() # Here we must go into with the effect of C (so choice updated) AND deeper in the decision tree (DFS) so we must reduce the number of letters
            # Undo C
            letters.insert(i, letter)
            choice.pop()
    _permut()
    return res

print(len(permute("MARTY")))


# Think about it like a tree. Going down a edge means a) adding the letter to the chocie and removing the letter from the remaining available letters
# For me, the difference between backtracking and DFS is that backtracking handles an implicit tree and DFS deals with an explicit one.
# This seems trivial, but it means a lot. When the search space of a problem is visited by backtracking, the implicit tree gets traversed and pruned in the middle of it.
# Yet for DFS, the tree/graph it deals with is explicitly constructed and unacceptable cases have already been thrown, i.e. pruned, away before any search is done.
#
