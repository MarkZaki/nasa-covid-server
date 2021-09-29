def binary_search(arr, left, right, key, value):
    if right >= left:
        mid = left + (right - left) // 2
        value = value.lower()
        current = arr[mid][key].lower()
        print(current)
        if current == value:
            return mid
        elif current > value:
            return binary_search(arr, left, mid - 1, key, value)
        else:
            return binary_search(arr, mid + 1, right, key, value)
    else:
        return -1
