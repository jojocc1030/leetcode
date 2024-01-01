/*
 * @lc app=leetcode.cn id=8 lang=java
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
class Solution {
    public int myAtoi(String s) {
       char[] toInt = s.toCharArray();
       int sign = 1; //记录正负号
       int max_boundry = Integer.MAX_VALUE / 10;
       int max_digit = Integer.MAX_VALUE % 10;
       int i = 0;
       int res = 0;
        
       if(toInt.length == 0) return 0;  // ******** 重要！ 检验此时字符串是否已经结束！ 因为涉及到后续toInt[i]的合法性问题
       while (toInt[i] == ' ') {
        i ++;
        if(i == toInt.length) return 0;   // ******** 重要！ 检验此时字符串是否已经结束！ 因为涉及到后续toInt[i]的合法性问题
       }

       if (toInt[i] == '-') sign = -1;
       if(toInt[i] == '-' || toInt[i] == '+') i ++;

       for(int j = i; j < toInt.length; j++){
        if(toInt[j] > '9'|| toInt[j] < '0') break;
        if(res > max_boundry ||(res == max_boundry && (toInt[j] - '0') > max_digit)){
            return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }
        res = res * 10 + (toInt[j] - '0');       
       }
       return res * sign; 

    }
}
// @lc code=end

