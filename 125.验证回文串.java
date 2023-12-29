/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// 标准化字符串：
// 使用 toLowerCase 方法将字符串转换为小写，以确保在比较时不区分大小写。
// 使用 replaceAll("[^a-z0-9]", "") 移除所有非字母和非数字字符，只保留小写字母和数字。

//双指针判断回文字符串



// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        String s_change = s.toLowerCase();
        s_change = s_change.replaceAll("[^a-z0-9]", "");
        char[] s2c = s_change.toCharArray();
        for (int i = 0, j = s2c.length - 1; i < j; i ++, j--){
            if(s2c[i] != s2c[j]){
                return false;
            }
        }
        return true;

    }
}
// @lc code=end

