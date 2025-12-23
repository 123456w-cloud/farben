# import functools
# import logging
#
# logging.basicConfig(level=logging.INFO)
#
#
# def log_decorator(func):
#     # @functools.wraps(func)  # 保留原函数元信息
#     def wrapper(*args, **kwargs):
#         logging.info(f"执行函数{func.__name__},参数：{args}, {kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"函数{func.__name__} 执行结果：{result}")
#         return result
#
#     return wrapper
#
#
# @log_decorator
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))
import copy

import loguru
from loguru import logger


def add(a, b):
    logger.info(f"计算{a}+{b}")
    return a + b


result = add(2, 3)
logger.info(f"结果{result}")


# print(add(2, 3))


def count_element_frequency(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency


nums = [1, 1, 1, 1, 1, 2, 3, 1, 3, 4]
# print(count_element_frequency(nums))
result = count_element_frequency(nums)
logger.info(f"次数{result}")


def deep_copy_response(response):
    return copy.deepcopy(response)


response = {"code": 200, "data": {"user": {"name": "李四", "age": 25}}}
copied = deep_copy_response(response)
copied["data"]["user"]["age"] = 30
print(response["data"]["user"]["age"])
print(copied["data"]["user"]["age"])


def calculate(a, b, operator):
    try:
        """最基本的计算函数"""
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "错误：除数不能为0"
            return a / b
        else:
            return "错误：不支持的运算符"
    except ValueError:
        print("请输入有效数字")


# 测试用例（简单写几个）
print(calculate("a", 5, '+'))  # 15
print(calculate(10, 5, '-'))  # 5
print(calculate(10, 0, '/'))  # 错误：除数不能为0
