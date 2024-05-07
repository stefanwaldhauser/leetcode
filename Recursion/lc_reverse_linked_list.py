# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    start = reverse_list(head.next)
    # --h-> 1 -> h.next -> 2 ->h.next.next -> 3
    # The new end is 2 after reversing so we need to point h.next.next to h and then h.next to None
    head.next.next = head
    head.next = None
    return start

# Assume that n is the list's length
# Time Complexity : O(N)
# Space Complexity: O(N)
