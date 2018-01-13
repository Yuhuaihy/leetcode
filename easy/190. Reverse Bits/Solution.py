class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = str(bin(n))
        result = 0
        count = 0
        num = 32- len(s) + 2  # for 123, s = 0b1111011, delete 0b
        temp = "0"*num
        s = temp + s[2:] #add 0 to 32 bits
        for i in s:
            result += int(i) * pow(2,count)
            count += 1
        return result
