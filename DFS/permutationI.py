class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        solution = []
        self.backtrace(nums, solution, [], set())
        return solution

    def backtrace(self, nums, solution, curr_permu, curr_permu_set):
        if len(curr_permu) == len(nums):
            solution.append(list(curr_permu))
        for x in nums:
            if x in curr_permu_set:
                continue
            curr_permu.append(x)
            curr_permu_set.add(x)
            self.backtrace(nums, solution, curr_permu, curr_permu_set)
            curr_permu.pop()
            curr_permu_set.remove(x)

s = Solution()
s.permute([1,2,3])
