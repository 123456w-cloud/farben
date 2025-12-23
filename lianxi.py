class Solution:
    # 整数反转
    def reverse_integer(self, number):
        h = number // 100
        t = number % 100 // 10
        z = number % 100 % 10
        return (z * 100 + t * 10 + h)

    def reverse_integer_math(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return sign * reversed_num

    def reverse_integer_safe(self, x: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        sign = 1 if x > 0 else -1
        x = abs(x)
        reverse_num = 0
        while x > 0:
            digit = x % 10
            # 检查溢出：reversed_num * 10 + digit > INT_MA  6
            if reverse_num > (int_max - digit) // 10:
                return 0
            reverse_num = reverse_num * 10 + digit
            x //= 10
        reverse_num *= sign

        # 检查结果是否在32位整数范围内
        if reverse_num < int_min or reverse_num > int_max:
            return 0
        return reverse_num

    def reverse_integer_string(self, x) -> int:
        str_x = str(x)
        if str_x[0] == '-':
            return -int(str_x[1:][::-1])
        else:
            return int(str_x[::-1])

    # 合并排序数组
    def merge_sort_array(self, arr, arr1):
        try:
            i, j = 0, 0
            m, n = len(arr), len(arr1)
            list1 = []
            while i < m and j < n:
                if arr[i] < arr1[j]:
                    list1.append(arr[i])
                    i += 1
                elif arr[i] == arr1[j]:
                    list1.append(arr[i])
                    i += 1
                    list1.append(arr1[j])
                    j += 1
                else:
                    list1.append(arr1[j])
                    j += 1
            while i < m:
                list1.append(arr[i])
                i += 1
            while j < n:
                list1.append(arr1[j])
                j += 1
            return list1
        except Exception as e:
            return f"错误：{e}"

    # 旋转字符串1
    def rotate_string(self, strings, offset):
        n = len(strings)
        if n > 0 and offset > 0:
            offset %= n
            strings = strings[offset:] + strings[:offset]
            return strings
        elif n > 0 and offset < 0:
            offset = abs(offset)
            offset %= n
            # strings = strings[n - offset:] + strings[:n - offset] # 两种写法
            strings = strings[-offset:] + strings[:-offset]
            return strings
        else:
            return -1

    # 旋转字符串2
    def rotate_string1(self, s, offset1):
        if len(s) > 0:
            offset1 %= len(s)
            temp = (s + s)[len(s) - offset1:2 * len(s) - offset1]
            """# 得到原列表的两倍长度，通过切片取出旋转后的部分：
                # 起始索引: len(s) - offset
                # 结束索引: 2 * len(s) - offset
                """

            for i in range(len(temp)):
                s[i] = temp[i]


#
# if __name__ == '__main__':
#     # 数字反转
#     solution = Solution()
#     # num = 123
#     num = int(input("整数："))
#
#     # ans = solution.reverseInteger(num)
#     print("输入：", num)
#     # print("输出：", ans)
#     ans1 = solution.reverse_integer_math(num)
#     print("输出：", ans1)
#
#     num1 = 7463847412  # 2147483647
#     ans4 = solution.reverse_integer_safe(num1)
#     print("输出：", ans4)
#
#     string1 = input("输入：")
#     ans2 = solution.reverse_integer_string(string1)
#     print("输出：", ans2)
#     ans3 = input("输入任何形式：")
#     print(''.join(reversed(ans3)))  # reversed返回反转迭代器对象,要有承载
#     print(ans3[::-1])
# if __name__ == '__main__':
#     solution = Solution()
#
#     # 合并排序数组 有序
#     print("合并排序数组")
#     a, b = [1, 2, 3], [1, 4, 5]
#     print("内置：", solution.merge_sort_array(a, b))
#     # arr = list(input("数组："))
#     # arr1 = list(input())
#     # 修复输入处理
#     print("\n --- 手动输入测试 ---")
#     arr_input = input("输入第一个数组（用空格分隔的数字，如：1 2 3）：")
#     arr1_input = input("输入第二个数组（用英文逗号分隔的数字，如：1,4,5）：")
#
#     # 将输入转换为整数列表
#     arr = [int(x) for x in arr_input.split()]
#     arr1 = [int(x) for x in arr1_input.split(',')]
#
#     # 确保数组是已排序的
#     arr.sort()
#     arr1.sort()
#     merge_ans = solution.merge_sort_array(arr, arr1)
#     print("数组合并：", merge_ans)

if __name__ == '__main__':
    # 旋转字符串
    # solution = Solution()
    # strings = input("字符串：")
    # offset = int(input("偏移量："))
    # print(solution.rotate_string(strings, offset))
    s = ["a", 'b', 'c', 'e', 'f', 'g']
    offset1 = 3
    solution = Solution()
    solution.rotate_string1(s, offset1)
    print("输入：s = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],", "offset1=", offset1)
    print("输出：", s)
