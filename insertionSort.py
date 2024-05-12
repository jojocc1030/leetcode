def insertion_Sort(arr):
    # 前i-1个元素已经有序，需要对第i个元素确定其插入位置
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_Sort(arr=[2,2,5,3,2,5,6,3])) 