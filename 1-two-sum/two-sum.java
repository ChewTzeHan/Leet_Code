class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            //System.out.println(i);
            for(int j = 0; j < nums.length; j++){
                if( j == i){
                    continue;
                }

                if ((nums[i] + nums[j]) == target){
                    //System.out.println(i);
                    //System.out.println(j);
                    int result[] = {i, j};
                    return result;
                }
            }
        }
        //System.out.println(nums);
        return nums;
    }
}