class Solution {
    public int reverse(int x) {
       //2147483647  Integer.MAX_VALUE
        double max = Integer.MAX_VALUE / 10.0;
        double min = Integer.MIN_VALUE / 10.0;
        
        int result = 0;
        int tail = 0,temp = 0;
        while(x != 0){
        tail = x % 10;
            if( (x > 0 && result > max - tail/10.0) || (x<0 && result < min - tail/10.0)){
            return 0;
        }
        temp = result * 10 + tail;
        result = temp;
        x = x/10;
        }
        return result;
        
    }
}

/*
Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/
