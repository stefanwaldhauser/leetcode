# We do NOT store a heap as a binary tree here, as the memory
# for the pointers can outweigh the size of the keys which is the data
# we are intersted in. For example if pointer is 64 bit and we store just
# keys of 32 bit integers, we waste a lot of memory.

# Instead: We store data as an array of keys, and use the position of
# the keys to implicitely play the role of the pointers

# https://www.youtube.com/watch?v=fJORlbOGm9Y

# if node is at position i, thn its left child is stored at 2*i + 1 and its right at 2 * i + 2
# the parent of a node can be found by the reverse operation round_down(i-1/2)

#             20
#        13           9
#      8    5       3    7
#     6  2  1

# is stored as
# [ 20| 13| 9| 8| 5| 3| 7| 6| 2| 1]
# 0  1    2  3  4  5  6  7  8  9

# children of 8 at position 3, are at position 7 and position 8 which is exactly 6 and 2
# parent of 8 position 3 is at position 1 which is exactly 13


# Some Tree Math
# - the number of nodes in a level h is pow(2,h), so at level 0 (root), one node, then at level 1 two nodes, at level 2 4 nodes and so on
# - The total number of nodes is therefore if all levels are filled
# the geometric series N = pow(2,0) + pow(2,1) + pow(2,2) + ... + pow(2,h)
# Using the formulare for geometric series and simplifying we find that the toatal number of nodes
# N = pow(2,h+1)-1 (there is no magic here, just used geometric series formula)

# Maximum size of heap of size h (meaning h is completely fulled)
#  N = pow(2,h+1)-1
# Minimum size of heap of size h(meaning just one node in level h, just to reach level h)
# From the above for a level h-1 heap we get the number of nodes is N = pow(2,(h-1)+1)-1 = pow(2,h) -1
# Now we have one extra node to get to level h again, so the nodes are N = pow(2,h)
# --> A heap / complete binary tree of height h has min N= pow(2,h) nodes and max N=pow(2,h+1)-1 nodes
# so pow(2,h) <= N < pow(2,h+1) (if we ignore the little -1 we can just make it a < instead of a <=)
# lets solve both sizes for H
# log2(pow(2,h))) <= log2(N) <= log2(pow(2,h+1))
# h <= log2(N) < h +1 ---> THE HEIGHT OF THE HEAP IS O(logN)
# The logarithmic height ensures that operations like insertion, deletion, and accessing the min/max element can be done in O(logN)
#
# Die höhe eines heaps / complete binary trees ist O(log(N)), die laufzeit aller operationen skaliert mit der hoehe des baumes, da die hoeh
# logarithmisch begrenzt ist zur anzahl der knoten im heap, ist es folglich auch die laufzeit von insert, deletion und access



import math
class MinArrayBasedHeap:
    def __init__(self) -> None:
        self.a = []

    def parent(self, i):
        parent_i = math.floor((i-1)/2)
        if parent_i < 0:
            return (None, None)
        return (parent_i, self.a[parent_i])

    def left_child(self, i):
        left_child_i = 2 * i + 1
        if left_child_i >= len(self.a):
            return (None,None)
        return (left_child_i, self.a[left_child_i])

    def right_child(self, i):
        right_child_i = 2 * i + 2
        if right_child_i >= len(self.a):
            return (None,None)
        return (right_child_i, self.a[right_child_i])

    def __swap(self, i, j):
        temp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = temp


    # Bubble up until no longer being dominated by the parent. The parent was before smaller than both children
    # if you now swap with the parent because you want to be smaller than the parent, it is guaranteed
    # that you are also smaller than the other existing child, as the parent was already smaller than it and
    # now you are smaller than the parent.
    def __bubble_up(self, i):
        n = self.a[i]
        (parent_i, parent) = self.parent(i)
        if parent_i is None:
            return # at the root (can not bubble up further)
        # index is in wrong position as the parent should be smaller in a min heap
        # for max heap just this condition needs to be changed
        if parent > n:
            self.__swap(parent_i, i) # swap parent and child (child now at parent index)
            self.__bubble_up(parent_i)

    def __sink_down(self,i):
        if(len(self.a) == 0):
            return
        n = self.a[i]
        left_child_i, left_child = self.left_child(i)
        right_child_i, right_child = self.right_child(i)

        smallest_child_i = None
        if left_child is not None and (right_child is None or left_child < right_child):
            smallest_child_i = left_child_i
        elif right_child is not None: # either left child was none or it was larger than the right child, anyway right child survives if it exists
            smallest_child_i = right_child_i

        if smallest_child_i is not None and n > self.a[smallest_child_i]:
            self.__swap(smallest_child_i, i)
            self.__sink_down(smallest_child_i)



    # Runtime: O(logN) where N is the total number of nodes in the heap, as it scales with height
    # In the worst case we have to bubble up the whole way to the top
    def insert(self, n):
        self.a.append(n)
        self.__bubble_up(len(self.a)-1)


    @staticmethod
    # Runtime len(l) * O(log N) = O(N log N) as each each node in l scales with the height where N is the total number of nodes
    def make_heap(l):
        heap = MinArrayBasedHeap()
        for n in l:
            heap.insert(n)
        return heap

    def extract_min(self):  # Runtime: O(logN) where N is the total number of nodes in the heap, as it scales with height
        if len(self.a) == 0:
            return None
        minimum = self.a[0]
        self.__swap(0, len(self.a)-1)
        self.a[-1:] = [] # deletes last element
        self.__sink_down(0)
        return minimum


def heap_sort(l) :
    min_heap = MinArrayBasedHeap.make_heap(l) #O(n logn)
    sorted_l = []
    minimum = min_heap.extract_min() # O(n log n)
    while(minimum is not None):
        sorted_l.append(minimum)
        minimum = min_heap.extract_min()
    return sorted_l

print(heap_sort([5,3,7,3,2,7,2,-1,-6,1]))
