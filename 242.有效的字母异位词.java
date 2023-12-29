/*
 * @lc app=leetcode.cn id=242 lang=java
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
import java.util.HashMap;


/** updated version */
// 优化1：仅使用一个map 实现算法，即统计s字符频数时 +1 ，统计t字符频数时-1；
// 优化2：先比较两个字符串长度，不一致直接返回false;
// 优化3：dic.getOrDefault(s.charAt(i), 0) 初始化字典   Returns the value to which the specified key is mapped, or defaultValue if this map contains no mapping for the key.



class Solution_1{
    public boolean isAnagram(String s, String t){
        if( s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> dic = new HashMap<>();
        char[] s_c = s.toCharArray(), t_c = t.toCharArray();
        for(char c : s_c){
            dic.put(c, dic.getOrDefault(c, 0) + 1);
        }
        for(char c : t_c){
            dic.put(c, dic.getOrDefault(c, 0) - 1);
        }
        for(int i : dic.values()){
            if ( i != 0 ) return false;
        }

        return true;

    }
}




/** initial version */


class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> s_h = new HashMap<>();
        HashMap<Character, Integer> t_h = new HashMap<>();
        char[] s_c = s.toCharArray();
        char[] t_c = t.toCharArray();
        for(char c : s_c ){
            if(s_h.get(c) == null){
                s_h.put(c, 0);
            }
            s_h.put(c, s_h.get(c) + 1);
        }

        for(char c : t_c){
            if(t_h.get(c) == null){
                t_h.put(c, 0);
            }
            t_h.put(c, t_h.get(c) + 1);
        }

        return s_h.equals(t_h);
    }
}
// @lc code=end

