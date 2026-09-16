# Program to implement binary search using a recursive function

def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)


arr = [10, 20, 30, 40, 50, 60, 70]
key = int(input("Enter the element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")