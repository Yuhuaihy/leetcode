class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                index = stack[-1][1]
                result[index] = i - index
                stack.pop()
            stack.append([temperatures[i],i])
        return result
