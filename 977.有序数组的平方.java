/*
 * @lc app=leetcode.cn id=977 lang=java
 *
 * [977] 有序数组的平方
 */

// @lc code=start
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] sqare = new int[nums.length];
        int left = 0, right = nums.length -1;
        int i = nums.length - 1;
        while (left <= right) {
            if(nums[left] * nums[left] < nums[right] * nums[right]){
                sqare[i --] = nums[right] * nums[right];
                right --;
            }
            else{
                sqare[i --] = nums[left] * nums[left];
                left ++;
            }
        }

        return sqare;
    }
}
// @lc code=end

