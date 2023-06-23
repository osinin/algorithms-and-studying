"""
Вывести следующее число из списка после таргера
"""
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 8
nearest = {}


def binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            try:
                return arr[mid+1]
            except:
                print("Target value is the last in the list")
                return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
            nearest[mid] = (arr[mid] - target)
        else:
            high = mid - 1
            nearest[mid] = (arr[mid] - target)
    filtered_nearest = dict(filter(my_filtering_function, nearest.items()))
    print(filtered_nearest)
    sorted_nearest = sorted(filtered_nearest.items(), key=lambda x: x[1], reverse=True)
    try:
        return arr[sorted_nearest[0][0]]
    except:
        -1


def my_filtering_function(pair):
    key, value = pair
    if value > 0:
        return True  # keep pair in the filtered dictionary
    else:
        return False  # filter pair out of the dictionary


h = binary_search(arr, target)
print(h)

