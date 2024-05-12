def selectionSort(arr):
    # 前i个元素是有序的,因此j从i+1开始
    n = len(arr)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            tmp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = tmp

    return arr

arr = [1,42,6,7,3,5]
print(selectionSort(arr))