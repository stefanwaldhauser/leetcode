# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import List

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list2.next, list1)
        return list2

# Der Trick ist hier anzunehmen, dass das mergeTwoLists klappt wenn einer der listen ein Knoten, der Kopf fehlt. Alles was ich dann tun muss,
# ist den kleineren der beiden Köpfe zu nehmen und mit dem gemergeten rest u verbinden

# Time Complixity: O(n+m)
# Space Complexity: O(n+m)

# Time complexity : O(n+m)
# Because each recursive call increments the pointer to l1 or l2 by one (approaching the dangling null at the end of each list), there will be exactly one call to mergeTwoLists per element in each list. Therefore, the time complexity is linear in the combined size of the lists.
# Space complexity : O(n+m)
# The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, so n+mn + mn+m stack frames consume O(n+m) space.

# For anyone reading this... study this problem! It's a critical piece of many, many bigger problems to know that you can merge in linear time (MergeSort comes to mind, but also merging K sorted lists etc).
