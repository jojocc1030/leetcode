/*
 * @lc app=leetcode.cn id=209 lang=java
 *
 * [209] 长度最小的子数组
 */

// @lc code=start
class Solution {
    public int minSubArrayLen(int target, int[] nums) { //滑动窗口方法解决问题
        int result = Integer.MAX_VALUE;
        int i = 0;  //滑动窗口起点
        int subLength = 0; //当前子序列长度
        int sum = 0;
        for(int j = 0; j < nums.length; j ++){
            sum += nums[j];
            while (sum >= target) {
                subLength = j - i + 1;
                sum = sum -nums[i];
                i ++;
                result = subLength < result ? subLength : result;
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }
}
// @lc code=end

