class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0
        length = len(nums)
        res = length
        for i in range(length) :
            res ^= (i ^ nums[i])
        return res