/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start

// O(N)复杂度 哈希表方法
import java.util.Map;
import java.util.HashMap;

class Solution_1 {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> hashtable =  new HashMap<Integer,Integer>();
       for(int i= 0; i < nums.length; i++){
        if(hashtable.containsKey(target - nums[i])){
            return new int[] {i, hashtable.get(target - nums[i])};
        }
        hashtable.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
 
    }
}



//O(n^2)复杂度 暴力法
class Solution_2 {
    public int[] twoSum(int[] nums, int target) {
        int[] targetSum = new int[2];
        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                if(nums[i] + nums[j] == target){
                    targetSum[0] = i;
                    targetSum[1] = j;
                    return targetSum;
                }
            } 
        }
        return targetSum;
    }
}
// @lc code=end


