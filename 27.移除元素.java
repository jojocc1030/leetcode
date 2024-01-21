/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        //双指针 + 数组 经典例题
        int p = 0;
        int q = 0;
        while (q < nums.length) {
            if(nums[q] != val) {
                nums[p] = nums[q];
                p ++;
            }
            q ++;
        }

        return p;
    }
}
// @lc code=end

