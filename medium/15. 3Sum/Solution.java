class Solution {
    
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        int l = nums.length;
        for (int i = 0 ; i < l-2 ; i++){
            if((i==0)||(nums[i]!=nums[i-1] && i>0)){
            int sum;
            sum = nums[i]*(-1);
            int low = i+1;
            int high = l-1;
            while(low<high){
            int twoSum = 0;
            twoSum = nums[low] + nums[high];
            if(sum == twoSum){
                result.add(Arrays.asList(nums[i],nums[low],nums[high]));
                low++;
                high--;
                while(nums[high]==nums[high+1] && high>0) high--;
                while(nums[low]==nums[low-1] && low < l-1) low++;
            }
            else if(sum < twoSum){
                high--;  
                while(nums[high]==nums[high+1] && high>0) high--;
            }
            else{
                low++;    
                while(nums[low]==nums[low-1] && low < l-1) low++;
            }
            
            }
        }
        }
