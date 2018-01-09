class Solution {
    public int rob(int[] nums) {
        int yes=0;
        int no=0;
        int temp;
        for(int i= 0; i<nums.length;i++){
            temp = Math.max(yes,no); // no
            yes = nums[i] + no;
            no = temp;
        }
        return Math.max(yes,no);
        
    }
}
