
def Bubble_sort(arr):
    # 冒泡排序可以保证每次尾部的元素是有序的
    # 升序
    n = len(arr)
    for i in range(n):
        flag = True
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                flag = False
        if flag:
            break
    return arr

arr = [2,1,31,4,5] 
print(Bubble_sort(arr))