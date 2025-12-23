def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr


print(bubble_sort([3, 4, 1, 2]))


def sortd(arr):
    n = len(arr)
    if n <=1:
        return arr

    mid = n // 2
    l, r, p = [], [], []
    for i in arr:
        if i == arr[mid]:
            p.append(i)
        elif i < arr[mid]:
            l.append(i)
        else:
            r.append(i)
    return sortd(l) + p + sortd(r)


print(sortd([0, 3, 1, 2, 5, 1, 4]))


def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(binary_search([1, 2, 4, 5, 6], 6))

a = [1,1,33,33]
b = list(set(a))
print(b)
c = list(dict.fromkeys(a))
print(c)
d = []
for i in a:
    if i not in d:
        d.append(i)
print(d)

e = 'abcdefjhijk'
f=e[::-1]
e1 = ''.join(reversed(e))
print(f)
print(e1,"e")
j = ''
for i in e:
    j = i + j
print(j)

h = 'abcdef123321fedcba'
i = [a.lower() for a in h if a.isalnum()]
print(h == h[::-1])

j = [1,32,54,0]
k = [1,2,32,"k"]
print(list(set(j)^set(k)))
l = []
for i in j:
    if i not in k :
        l.append(i)
for i in k:
    if i not in j :
        l.append(i)
print(l,"k")
