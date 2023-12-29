/*
 * @lc app=leetcode.cn id=387 lang=java
 *
 * [387] 字符串中的第一个唯一字符
 */

// @lc code=start

import java.util.HashMap;

class Solution {
    public int firstUniqChar(String s) {
        char[] str2c = s.toCharArray(); //string to char array 的方法
        HashMap<Character, Boolean> hashtable = new HashMap<>();
        for(int i = 0; i < str2c.length; i++){
            hashtable.put(str2c[i], ! hashtable.containsKey(str2c[i]));
        }
        for (int i = 0; i < str2c.length; i++){
            if(hashtable.get(str2c[i])) return i;
        }
        return -1;


    }
}
// @lc code=end

