/*
 * @lc app=leetcode.cn id=28 lang=java
 *
 * [28] 找出字符串中第一个匹配项的下标
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        char[] HayArr = haystack.toCharArray();
        char[] NeedArr = needle.toCharArray();
        // int sign = -1;
        
        for (int i = 0; i <= HayArr.length - NeedArr.length; i ++){  // 若要成功匹配 i 至少要从（ HayArr.length - NeedArr.length ）开始匹配
            int j = 0;
            // if(HayArr[i] == NeedArr[j]) sign = i;
            int tmp = i;
            while (HayArr[tmp] == NeedArr[j]) {
                if (j == NeedArr.length - 1) return i;
                // if (tmp == HayArr.length - 1) return -1;   // 需要考虑到Hayarr已经结束，但是NeedArr还未结束的情况
                tmp ++;
                j ++;
            }
            // sign = -1;
           
        }

        return -1;

    }
}
// @lc code=end

