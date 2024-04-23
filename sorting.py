def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

num = [64, 19, 25, 99, 36, 50, 86]
bubble_sort(num)
print("Sorted array:", num)
