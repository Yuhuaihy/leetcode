class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> counter = new HashMap<Integer,Integer>();
        int n = nums1.length;
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i<n; i++ ){
            if(!counter.containsKey(nums1[i]) ){
                    counter.put(nums1[i],1);
                }
            else{
                    counter.put(nums1[i],counter.get(nums1[i])+1);
                }
            }
        for( int i = 0; i < nums2.length; i++){
            if(counter.containsKey(nums2[i])){
                int c = counter.get(nums2[i]);
                if(c ==1){
                    counter.remove(nums2[i]);
                    result.add(nums2[i]);
                }
                else{
                    result.add(nums2[i]);
                    counter.put(nums2[i],c-1);
                }
                
            }
        }
        
        int[] r = new int[result.size()];
       for(int i = 0; i < result.size(); i++)
       {
           r[i] = result.get(i);
       }
        return r;
            
        }
    }

