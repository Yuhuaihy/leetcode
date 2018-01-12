#Given an array of integers, every element appears twice except for one. Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A^B^B = A
        result = nums[0]
        for i in range (1,len(nums)):
            result = result^nums[i]
        return result
    
    
    class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numberSet = set(nums)
        list1 = list(numberSet)*2
        for n in nums:
            list1.remove(n)
        return list1[0]
        
    class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numberSet = list()
        for n in nums:
            if n not in numberSet:
                numberSet.append(n)
            else:
                numberSet.remove(n)
        
        return numberSet[0]
