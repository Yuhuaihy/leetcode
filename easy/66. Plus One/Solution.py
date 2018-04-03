class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] + 1 < 10:
            digits[-1] = digits[-1] + 1
            return digits
           
        c = 1
        n = len(digits)
        if n == 1:
            return [1,0]
        
        digits = list(reversed(digits))
        digits[0] = 0
        for i in range(1,n):
            temp = digits[i]
            digits[i] = (digits[i] + c) % 10
            c = int((temp + 1)/10)
            if not c:
                break
        if c:
            digits.append(1)
        return list(reversed(digits))
        #Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
