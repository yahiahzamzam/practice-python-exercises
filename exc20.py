a = [1, 3, 5, 30, 42, 43, 500]

num = int(input("enter a number to be found"))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while True:
        mid = (low + high) // 2
        arr[mid] = int(arr[mid])
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return None


print(f"Test-enter 5_expect 2: {binary_search(a, num)}")
num = int(input("enter a number to be found"))
ordered_lst: list[int]
ordered_lst = list(input("Please enter your list"))
print(binary_search(ordered_lst, num))
