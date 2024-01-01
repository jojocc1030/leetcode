/*
 * @lc app=leetcode.cn id=38 lang=java
 *
 * [38] 外观数列
 */

// @lc code=start

import java.util.ArrayList;

class Solution {
    public String countAndSay(int n) {
        /*********************************以下为改进后版本************************** */
        // 1. 使用** 双指针 ** 思想！！！
        //2. 对 Integer 和 字符串之间的转换不熟练！！ 学会使用StringBuilder

        String ans = "1";
        for (int i = 2; i <= n; i++){
            StringBuilder sb = new StringBuilder();

            int start = 0;
            int pos = 0; //双指针！！！

            while (pos < ans.length()) {
                while (pos < ans.length() && ans.charAt(start) == ans.charAt(pos)) {
                    pos ++;
                }

                sb.append(Integer.toString(pos - start)).append(ans.charAt(start));

                start = pos;
            }

            ans = sb.toString();



        }
        return ans;
       
       
       
       
        /************************以上为原始答案，评价为 ： 史 ****************************/

       
        // String str = "1";
        // for (int i = 2 ; i <= n; i++){
        //     ArrayList<Integer> countAndSay = new ArrayList<>();
        //     int count = 0;
        //     char[] str2ch = str.toCharArray();
        //     char flag = str2ch[0];
        //     for (int j = 0; j < str2ch.length; j++){
        //         if(str2ch[j] == flag && j < str2ch.length -1){
        //             count ++;
        //         }
        //         else if(str2ch[j] == flag && j == str2ch.length -1){
        //             count ++;
        //             countAndSay.add(count);
        //             countAndSay.add(str2ch[j] - '0');

        //         }
        //         else if(str2ch[j] != flag && j< str2ch.length -1){
        //             countAndSay.add(count);
        //             countAndSay.add(str2ch[j-1] - '0');
        //             flag = str2ch[j];
        //             count = 1;
        //         }
        //         else if(str2ch[j] != flag && j == str2ch.length -1){
        //             countAndSay.add(count);
        //             countAndSay.add(str2ch[j-1] - '0');
        //             countAndSay.add(1);
        //             countAndSay.add(str2ch[j] - '0');
        //         }
        //     }
        //     System.out.println(countAndSay.toString());
        //     if(!countAndSay.isEmpty())
        //         str = countAndSay.toString().replaceAll("\\s+", "")
        //         .replaceAll(",", "")
        //         .replaceAll("\\[", "")
        //         .replaceAll("]", "");
        //     else
        //         str = "11";
        // }

        // return str;

        /************************以上为原始答案，评价为 ： 史 ****************************/


        // 1. 使用** 双指针 ** 思想！！！
        //2. 对 Integer 和 字符串之间的转换不熟练！！
        
        /*********************************以下为改进后版本************************** */




    }
}
// @lc code=end

