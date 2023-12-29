# HashMap的相关题型

###  [387] 字符串中的第一个唯一字符

给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

 

示例 1：

输入: s = "leetcode"
输出: 0

示例 2:

输入: s = "loveleetcode"
输出: 2

示例 3:

输入: s = "aabb"
输出: -1

 

提示:

    1 <= s.length <= 105
    s 只包含小写字母


```java
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
```



### [1] 两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
 

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
```java
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
```

 **一些感悟** ：hashmap解题可以有效降低算法复杂度，解题关键在于想清楚谁是**key**,谁是**value**.