class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        start = 0
        width = len(nums)//2
        end = start + width
        while abs(end-start) > 1:
            end = (start + width) % len(nums)
            if nums[start] < nums[end]:
                start = end
            elif nums[start] > nums[end]:
                width //= 2
            else:
                break
        curr_min = nums[start]
        for i in range(min(start, end), max(start, end)+1):
            if nums[i] < curr_min:
                curr_min = nums[i]
        return curr_min

s = Solution()
s.findMin([5,6,7,1,2,3,4])
