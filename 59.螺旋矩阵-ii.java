/*
 * @lc app=leetcode.cn id=59 lang=java
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int loop = 1;  //转圈数
        int start = 0; //每次循环的开始点
        int i = 0, j = 0;
        int count = 1; //填充数字
        while (loop <= n / 2) {
            for(j = start ; j < n - loop; j++){
                res[i][j] = count ++;
            } //左--->右

            for(i = start; i < n - loop ; i++){
                res[i][j] =  count ++;
            } //上-->下

            for(;j > start; j --){
                res[i][j] = count ++;
            } //右--->左

            for(; i > start; i--){
                res[i][j] = count ++;
            } //下-->上

            loop ++;
            start ++;
            i = start;  //注意 一轮循环结束后i的位置
        }
        if(n % 2 == 1) res[start][start] = n * n; 
        
        return res;
    }
}
// @lc code=end

