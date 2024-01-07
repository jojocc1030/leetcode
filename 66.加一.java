/*
 * @lc app=leetcode.cn id=66 lang=java
 *
 * [66] 加一
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        int pos = digits.length - 1; //数组末尾指针
        while (pos >= 0 && digits[pos] == 9) {
            digits[pos] = 0;
            pos --;
        }
        if(pos >= 0) {
            digits[pos] += 1;
            return digits;
        }
        else{
            int[] res = new int[digits.length + 1];
            res[0] = 1;
            return res;

        }

    }
}
// @lc code=end

