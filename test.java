// import dogs.Dog;

public class test {
    public static void main(String[] args) {
        Solution_350 i = new Solution_350();
        int[] nums1 = new int[]{1, 2, 2, 1};
        int[] nums2 = new int[]{2, 2};
        int[] res = i.intersect(nums1, nums2);
        for(int j : res){
            System.out.println(j);
        }



    }
}
