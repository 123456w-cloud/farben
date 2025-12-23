def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] == target:
            return mid
        else:
            r = mid - 1
    return -1


def sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = arr[len(arr) // 2]
        # l = [x for x in arr if x < mid]
        # r = [x for x in arr if x > mid]
        # p = [x for x in arr if x == mid]
        l, r, p = [], [], []
        for x in arr:
            if x == mid:
                p.append(x)
            elif x < mid:
                l.append(x)
            else:
                r.append(x)
    return sort(l) + p + sort(r)


print(sort([3, 2, 1, 4, 5, 8, 2, 3, 5]))

print(bubble_sort([3, 0, 1, 2]))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 0))
