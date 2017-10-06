class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_endhere = 0
        max_sofar = 0
        maxn = -float('inf')
        for i in xrange(len(nums)):
            max_endhere += nums[i]
            maxn = max(maxn, nums[i])
            if max_endhere < 0:
                max_endhere = 0
            if max_sofar < max_endhere:
                max_sofar = max_endhere
        if maxn < 0:
            return maxn
        else:
            return max_sofar

class Solution2(object):
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

nums = [-2, 1, -2, 4, -1, 2, 1, -5, 4]
bestsum = {}
cursum = {}
bestsum[0] = -2
cursum[0] = -2
n = 8
def solution3(n, bestsum, cursum, nums):
    if n in cursum:
        return cursum[n]
    if n not in cursum:
        cursum[n] = max(nums[n], nums[n] + solution3(n-1, bestsum, cursum, nums))
        bestsum[n] = max(cursum[n], bestsum[n-1])
        return cursum[n]

print solution3(n, bestsum, cursum, nums)
print cursum
print bestsum

    
