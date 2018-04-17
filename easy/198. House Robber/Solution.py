class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no = 0
        yes = 0
        
        for num in nums:
            temp = no
            no = max(yes, temp)   
            yes = max(num, num + temp)
            
        return max(yes, no)
             
