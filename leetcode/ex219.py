class Solution1(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct = {}
        for i in xrange(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = i
            elif i - dct[nums[i]] <= k:
                return True
            else:
                dct[nums[i]] = i
        return False
