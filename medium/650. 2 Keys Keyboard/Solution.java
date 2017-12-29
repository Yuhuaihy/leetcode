class Solution {
    public int minSteps(int n) {
       // prime number/ factor
        int sum = 0;
        for(int i = 2; i< n+1; i++){
            if(n%i==0){                
                n = n/i;
                sum += i;
                i = 1;
            }            
        }
        return sum;
    }
}
