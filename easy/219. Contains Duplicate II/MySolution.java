class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                if((i-map.get(nums[i]))<=k){
                    return true;
                }
                else{
                    map.remove(nums[i]);
                }
            }
            map.put(nums[i],i);
        }
     return false;   
    }
}
/////use hashset
//hashset contains unique elements
public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i-k-1]);   // remove first element , k-size set
            if(!set.add(nums[i])) return true;  // when can't add, same element appears
        }
        return false;
 }
