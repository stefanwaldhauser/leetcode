# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None: # No node or one node
        return head
    swapped_rest = swap_pairs(head.next.next)
    # lets call the first two nodes a,b, we need to swap them
    a = head
    b = head.next
    b.next = a
    a.next = swapped_rest
    return b


# At each step of the recursion our input size will decrease by 2. The "cost" of swapping two nodes is O(1) each step
# So if n is the total length of the list the time complexity is n/2 * O(1) = O(n)
# The total number of recursive calls is n/2, so the height of the recursive tree is n/2. At each recursion
# step we use O(1) space as we just exchange pointers so the the space complexity is n/2 * O(1) = O(n)
