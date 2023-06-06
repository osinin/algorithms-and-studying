def binary_search(arr, target):
    arr = sorted(arr)
    print(f'sorted array: {arr}')
    low = 0
    high = len(arr) - 1
    print(f'high: {high}')
    while low <= high:
        mid = (low + high) // 2
        print(f'mid: {mid}')
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            print('mid < target')
            low = mid + 1
        else:
            print('mid > target')
            high = mid - 1
    return -1


arr = [23, 45, 1, 34, 4, 99, 5, 17]
target = 99

h = binary_search(arr, target)
print(h)

