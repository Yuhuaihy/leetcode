class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        # nums[i] = nums[ (i + k) % n]
        start = 0
        nex = 0
        count = 0
        while count < n:
            nex = start
            prev = nums[start]
            while(True):
    
                nex = ( nex + k ) % n
                temp = nums[nex]
                nums[nex] = prev
                current = nex
                prev = temp
                count = count + 1
                
                if current == start:
                    break
            start = start + 1
                
