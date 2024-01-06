/*
 * @lc app=leetcode.cn id=26 lang=java
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {  //经典双指针问题
        int p = 0;
        int q = 1;
        while (q < nums.length) {
            if(nums[p] != nums[q]) {
                if(q - p > 1) nums[++ p] = nums[q]; //优化速度，避免nums[p+1] 和nums[q]在原地址进行复制
                else p ++;
            }
            q ++;
            
        }
        return p + 1;
    }   
}
// @lc code=end

