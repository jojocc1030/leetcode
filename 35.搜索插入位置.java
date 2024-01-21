/*
 * @lc app=leetcode.cn id=35 lang=java
 *
 * [35] 搜索插入位置
 */

// @lc code=start
class Solution {
    public int searchInsert(int[] nums, int target) {
        
        //判断最大最小值情况
        if(nums.length == 0 || target < nums[0]) return 0;
        if(target > nums[nums.length - 1]) return nums.length;

        //二分法
        int left = 0;
        int right = nums.length - 1;
        int mid = left + (right - left) / 2;
        while (left <= right) {
            mid = left + (right - left) / 2 ;
            if(target == nums[mid]) return mid;
            else if(target < nums[mid]){
                right = mid -1;
            }
            else if(target > nums[mid]){
                left = mid + 1;
            }
        }

        //此时若没有return 则说明nums中不存在target，现在进行插入操作

        return target > nums[mid] ? mid + 1 : mid;
    }
}
// @lc code=end

