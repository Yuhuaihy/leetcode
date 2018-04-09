class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n in d.keys():
                d[n] = d[n] + 1
                
            else:
                d[n] = 1
                
            if d[n] > len(nums) / 2:
                    return n
                
        return None
        ###sort
