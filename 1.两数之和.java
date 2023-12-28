/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] targetSum = new int[2];
        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                if(nums[i] + nums[j] == target){
                    targetSum[0] = i;
                    targetSum[1] = j;
                    return targetSum;
                }
            } 
        }
        return targetSum;
    }
}
// @lc code=end

