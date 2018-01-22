class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n < 3:
            return 0
        elif n == 3:
            return 1
        else:
            count = [True]*n
            # i*i < n
            #  j*j +j(2j,3j)
            i = 2;
            while(i*i < n):
                if count[i]:
                    for j in range (i*i,n,i):
                        count[j] = False
                i +=1
                              
            for i in count[2:]:
                if i:
                    result +=1
            return result
                
                
