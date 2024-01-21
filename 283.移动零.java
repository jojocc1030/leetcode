/*
 * @lc app=leetcode.cn id=283 lang=java
 *
 * [283] 移动零
 */

// @lc code=start


/** 双指针法： p 指向第一个0， q指向第一个非0，交换 */
class Solution {
    public void moveZeroes(int[] nums) {
        int p = 0;
        int q = 0; //双指针
        while (q < nums.length) {
            if(nums[p] != 0 && nums[q] != 0){  //寻找第一个为0的下标
                p ++;
                q ++;
            }

            else if(nums[p] == 0 && nums[q] == 0) q ++; //p找到第一个为0的元素下标，q继续后移
            else if(nums[p] == 0 && nums[q] != 0){  // 此时p指向第一个0，q指向第一个非0
                nums[p] = nums[q];
                nums[q] = 0;
                p ++;
                q ++;
            }
            
       
            
        }

    

    }
}
// @lc code=end

