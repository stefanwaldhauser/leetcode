class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort in descending order by position
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        # We process cars from right to left (closest to target first)
        # If a car behind reaches target faster (less time) than the car in front,
        # it means they will collide and form a fleet moving at the slower speed
        # of the car in front

        for pos, spd in cars:
            # Calculate time to reach target
            further_car_target_inh = (target - pos) / spd

            # If stack is empty or it takes the further car longer,
            # they will not meet and form a new fleet
            if not stack or further_car_target_inh > stack[-1]:
                stack.append(further_car_target_inh)
            # If it takes the further car less time, they will have met
            # and merged into the fleet of the closer car

        return len(stack)

# Runtime: Sorting O(n log n), loop O(n) -> O(n log n) + O(n) = O(n log n)
# Space: O(n)
