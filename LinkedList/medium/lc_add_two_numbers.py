# Definition for singly-linked list.
from typing import Optional

# Given two !non-empty! linked lists l1, l2 where number of nodes in each list [1,100]
# Each list represents the digits of an integer in REVERSED order
# Compute the sum of the two numbers
# l1: 2->4->3 is number 342
# l2: 5->6->4 is number 463
# output: 7 -> 0 -> 8 which represents 342 + 465 = 807



# 0 <= Node.val <= 9 // Numbers from 0 to 9
# Guaranteed that list represents a number that does not have leading zeros

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def sum(list_a, list_b, carry):
            # base case: list_a and list_b are done
            if list_a is None and list_b is None:
                if carry:
                    return ListNode(1, None)
                else:
                    return None


            val = carry + (list_a.val if list_a else 0) + (list_b.val if list_b else 0)
            list_a_rest = list_a.next if list_a else None
            list_b_rest = list_b.next if list_b else None

            if val >= 10:
                last_digit = val % 10
                return ListNode(last_digit, sum(list_a_rest, list_b_rest, True))
            else:
                return ListNode(val, sum(list_a_rest, list_b_rest, False))

        return sum(l1,l2, False)
