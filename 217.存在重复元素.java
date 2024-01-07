/*
 * @lc app=leetcode.cn id=217 lang=java
 *
 * [217] 存在重复元素
 */

// @lc code=start


import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> dic = new HashSet<>();
        for(int c : nums){
            if (dic.contains(c)) {
                return true;
            }
             else dic.add(c);
        }
        return false;

    }
}
// @lc code=end

