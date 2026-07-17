a = [1, 3, 5, 30, 42, 43, 500]

num = int(input("enter a number to be found"))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while True:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return None


print(f"Test-enter 5_expect 2: {binary_search(a, num)}")
