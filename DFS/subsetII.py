class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums = sorted(nums)
        solution = []
        self.backtracing(solution, nums, [], 0)
        return solution

    def backtracing(self, solution, nums, curr_set, curr_num_idx):
        if curr_num_idx >= len(nums):
            solution.append(list(curr_set))
            return
        next_num_idx = curr_num_idx
        while next_num_idx < len(nums) and nums[next_num_idx] == nums[curr_num_idx]:
            next_num_idx += 1
        for i in range(next_num_idx-curr_num_idx+1):
            curr_set.extend([nums[curr_num_idx]]*i)
            self.backtracing(solution, nums, curr_set, next_num_idx)
            for k in range(i):
                curr_set.pop()


s = Solution()
print s.subsetsWithDup([])
