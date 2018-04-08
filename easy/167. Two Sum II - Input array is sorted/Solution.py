class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or target < numbers[0]:
            return None
        d = {}
        for i in range(len(numbers)):
            goal = target - numbers[i]
            if goal < numbers[0]:
                return None
            if goal in d.keys():
                return [d[goal],i+1]
            else:
                d[numbers[i]] = i+1
            
