class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        low = 0 
        high = len(nums) - 1
        re = []
        if not nums:
            return 0
        while(1):
            while(nums[low] != val and low < (len(nums)-1)):
                low = low + 1
            while(nums[high] == val and high > 0):
                high = high -1
            if ( low < high):
                temp = nums[low]
                nums[low] = nums[high]
                nums[high] = temp
                low = low + 1
                high = high -1
                
            else:
                if low == (len(nums) - 1) and nums[low] != val:
                    return low + 1
                else:
                    return low
                
