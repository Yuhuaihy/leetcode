class Solution {
    public int maxSubArray(int[] nums) {
        int maxSoFar = nums[0];
        int maxNow = nums[0];
        for(int i = 1; i< nums.length;i++){
            maxNow = Math.max(nums[i],nums[i]+maxNow);
            maxSoFar = Math.max(maxSoFar,maxNow);
        }
        return maxSoFar;
        
    }
}
