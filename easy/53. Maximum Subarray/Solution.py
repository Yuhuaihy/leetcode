class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        sofar = nums[0]
        for i in range(1,len(nums)):
            current = max(current+nums[i],nums[i])
            sofar = max(current,sofar)
        return sofar
