class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]

# Consistent Order: Sorting ensures that each triplet is in a consistent order (e.g., smallest to largest), which can make it easier to compare triplets and identify duplicates
# So first we sort, and then we add them to a set
# Because nums is sorted this guaranteed that i < j < k implies nums[i] < nums[j] < nums[k]


class BestSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # We have to sort first, so we can use the problem to repeateadly solving two sum II
        nums.sort()
        # a triplet is only possible if there are two numbers left after ia
        for ia in range(len(nums)-2):
            # We do not want to calculate two sum II for the same target twice, therefore we need to makre sure only to consider each number once as target
            # We do this by picking the first in a series of duplicate numbers and skipping the rest
            # Its important to pick the first as a valid triple could contain the duplicates, so they need to be in the search space

            # If ia == 0 its guaranteed to be the first in a list of duplicates
            if ia > 0 and nums[ia] == nums[ia-1]:
                continue # skip as we have had this target value already

            # For each ia, a we now perform two sum II. The target will always be -a, so that b + c = -a which means a + b + c = a + (-a) = 0
            # The searchspace is the subarray to the right of ia, this allows us again to prevent duplicate
            # If the searchspace would be all indeces except ia, we would have repeated triplets in the solution
            ib = ia + 1
            ic = len(nums) - 1
            while ib < ic:

                if nums[ib]+nums[ic] > -nums[ia]:
                    ic -=1
                elif nums[ib]+nums[ic] < -nums[ia]:
                    ib += 1
                else:
                    res.append([nums[ia],nums[ib],nums[ic]])
                    # In two sum II we would have stopped here, but we want to look for ALL b+c that can add up to -a
                    ib += 1
                    ic -= 1

                    # Again we only want to consider the first in a series of duplicates so we skip those!
                    while ib < ic and nums[ib] == nums[ib-1]:
                        ib +=1
                    while ib < ic and nums[ic] == nums[ic+1]:
                        ic -= 1
        return res
