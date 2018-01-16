class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = {}
        i = 0
        l = len(nums)
        if t < 0:
            return False
        for i in range(l):
            bucket = nums[i]/(t+1) 
            if  bucket in d:
                return True
            if bucket+1 in d:
                if abs(nums[i] - d[bucket+1]) <= t:
                    return True
            if bucket-1 in d:
                if abs(nums[i] - d[bucket-1]) <= t:
                    return True
            d[bucket] = nums[i]
            if len(d) > k:
                del(d[nums[i-k]/(t+1)])    #ensure d no bigger than k
        return False
