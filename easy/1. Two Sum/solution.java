class Solution {

	public static void main(String args[]){
		Scanner s=new Scanner(System.in);
		int[] num=new int[20];
		int t;
		String str=s.nextLine();
		String[] arr=str.split(" ");
		int i=0;
		for(String a:arr){
			num[i]=Integer.parseInt(a);
			i+=1;	
		}     
        	t=s.nextInt();
        int[] re;
        re=twoSum(num,t);
       System.out.println("["+re[0]+","+re[1]+"]");  
    }
    static int[] twoSum(int[] nums, int target) {
        int[] re=new int[2];
        for(int i=0,j=0,s=0;i<nums.length-1;i++){
            j=i+1;  
            do{
        s=nums[i]+nums[j];  
        j+=1;	
	
            }while(s!=target && j!=nums.length);
            if(s==target){
                re[0]=i;
                re[1]=j-1;
               return re; 
            }
}    
    return re;}
}
