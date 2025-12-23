# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.taobao.com")
# driver.maximize_window()
# sleep(3)
# element=driver.find_element(By.TAG_NAME, 'body')
# for _ in range(3):
#     element.send_keys(Keys.PAGE_DOWN)
#     sleep(0.5)
from datetime import datetime, timedelta


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


def quickly_sort(arr):
    n = len(arr)
    if n <= 1:
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
    return quickly_sort(l) + p + quickly_sort(r)


def count_line(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            count = 0
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    count += 1
            return count
    except Exception as e:
        print(f'{e}')


def shijian(a,b,c):
    print_time = datetime(a,b,c) + timedelta(days=2)
    print(print_time)


if __name__ == '__main__':
    print(bubble_sort([3, 2, 1]))
    print(binary_search([1, 2, 3], 3))
    print(quickly_sort([3, 3, 1, 1, 5, 5, 22, 11]))
    print(count_line("11.p"))
    shijian(2025,8,26)
