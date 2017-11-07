class Solution:
    """
    Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is
    closest to the given target.
    Return -1 if there is no element in the array.
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        left = 0
        right = len(A) - 1
        while right - left > 1:
            mid = (left + right)//2
            if target <= A[mid]:
                right = mid
            else:
                left = mid
        if target - A[left] <= A[right] - target:
            return left
        else:
            return right
