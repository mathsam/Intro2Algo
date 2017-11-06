class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        count_per_num = dict()
        for x in nums:
            if x in count_per_num:
                count_per_num[x] += 1
            else:
                count_per_num[x] = 1
        solution = []
        self.backtracing(count_per_num, solution, [])
        return solution

    def backtracing(self, count_per_num, solution, curr_permu):
        if not count_per_num:
            solution.append(list(curr_permu))
        for x in list(count_per_num.keys()):
            curr_permu.append(x)
            if count_per_num[x] == 1:
                count_per_num.pop(x)
            else:
                count_per_num[x] -= 1
            self.backtracing(count_per_num, solution, curr_permu)
            if x in count_per_num:
                count_per_num[x] += 1
            else:
                count_per_num[x] = 1
            curr_permu.pop()

s = Solution()
s.permuteUnique([1,1,2,2,3])
