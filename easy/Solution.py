class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return len(nums)
            
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i = i+1
                nums[i] = nums[j]
        return i+1
        # return nums[:i+1]
