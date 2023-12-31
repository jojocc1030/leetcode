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

 **一些感悟** ：hashmap解题可以有效降低算法复杂度，解题关键在于想清楚谁是`key`,谁是`value`.

# 整数相关题型

此类题型主要涉及到 **整数溢出** 问题 和 **字符串转整数** 问题

涉及例题： 

### [7] 整数反转

```java
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            if(rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && x % 10 > Integer.MAX_VALUE % 10)){
                return 0;
            }
            if(rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && x % 10 < Integer.MIN_VALUE % 10)){
                return 0;
            }
            int tmp = x  % 10;
            rev = rev * 10 + tmp;
            x = x/10;

        }
        return rev;

    }
}
```

### [8] 字符串转换整数 (atoi)

```java
class Solution {
    public int myAtoi(String s) {
       char[] toInt = s.toCharArray();
       int sign = 1; //记录正负号
       int max_boundry = Integer.MAX_VALUE / 10;
       int max_digit = Integer.MAX_VALUE % 10;
       int i = 0;
       int res = 0;
        
       if(toInt.length == 0) return 0;
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
```

总结为以下几点：

- 单个字符转整数：`res = '9' - '0'`
- 整数越界判断（在系统最多只能存32位情况下）<img src = "images\Snipaste_2023-12-31_13-39-10.png"/>
- `Integer.MAX_VALUE / Integer.MIN_VALUE` 表示java的最大/最小整数