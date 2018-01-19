class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        else:
            begin = 0
            leng = 0
            for i in range(len(s)):
                if s[i] in s[begin:i]:
                    temp = i - begin
                    if temp > leng:
                        leng = temp
                    begin = s[begin:i].index(s[i]) + 1 + begin
            last = i - begin + 1
            return leng if leng > last else last
                
                
                
   #begin is the start of the non-repeat list, i is the end
   # start  in list[begin:i]
  # when repeat
  # i is the index of repeated element (2nd)
  # leng = max(leng, i - begin)
  # begin becomes the index of first repeated element + 1, then find repeated element in list[begin:i]
    # no extra space
   
