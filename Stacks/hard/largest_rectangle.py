class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        # Starting from a bar x rectangle of height heights[x] can be formed until we hit a bar that has a strictly smaller height
        # We therefor need to find for each bar the next smaller bar. A classical use case of a monotonic stack
        # See https://medium.com/@keshavrathinavel/leetcodes-monotonic-stack-problems-and-how-to-solve-them-made-easy-1c73c2d6d437
        stack = []

        # VERY COOL LEARNING: COMBINES NEXT AND PREVIOUS SMALLER FOR THE POPPED ELEMENT IN ONE LOOP!

        # + 1 is crucial for handling histograms that extend to the end of the histogram
        # When i is len(heights) - 1, so they get added to the stack
        # So we need to iterate ONE more time so we can perform a calculation for those also!
        for i in range(len(heights) + 1):
            # Use height 0 for the additional position to handle remaining stack elements
            i_height = heights[i] if i < len(heights) else 0

            while stack and i_height < heights[stack[-1]]:
                # i is the index with the next smaller height
                height = heights[stack.pop()]
                # The key insight is now that because of the monotonic nature of the stack, the prev smaller elemenet
                # for that popped element is now sitting at the top of the stack as well

                # Think about: In the previous for loop iteration, you cleared the stack of all elements larger than the element you then appended to the stop of the stack
                # Therefore: Walking through the stack is always the previous smaller!!!!
                width = (i - stack[-1]) - 1 if stack else i
                area = height * width
                max_area = max(area, max_area)

            stack.append(i)
        return max_area

Runtime: O(n)
