/*
 * @lc app=leetcode.cn id=136 lang=java
 *
 * [136] 只出现一次的数字
 */

// @lc code=start

/** 显然可以用哈希表解决，但是需要O(n)个额外空间 */
/** 因此考虑用 **异或** 解决问题，
作者：力扣官方题解
链接：https://leetcode.cn/problems/single-number/solutions/242211/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 */



class Solution {
    public int singleNumber(int[] nums) {
       int flag = 0;
       for(int x : nums){
            flag ^= x;
       }
       return flag;

    }
}
// @lc code=end

