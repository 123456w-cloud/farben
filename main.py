"""
执行测试用例并生成Allure测试报告
步骤：
   1. 定义测试用例路径和报告输出路径
   2. 调用pytest执行测试用例并生成Allure原始数据
   3. 根据测试结果判断是否生成HTML报告
"""

import os
import shutil
import sys

import pytest


def run_test():
    test_directory = ["web_test.py"]  # 指定要执行测试的测试用例目录
    allure_report_directory = "./report/temp_jsonreport"  # 指定生成json数据保存目录
    html_report_directory = "./report/html"  # 指定生成html测试报告报错目录
    max_retries = 2  # 最大重试次数

    if os.path.exists(allure_report_directory):  # json_data  历史json数据保存目录
        shutil.rmtree(allure_report_directory)  # 删除目录及其内容
    os.makedirs(allure_report_directory, exist_ok=True)  # 重新创建空目录

    result = pytest.main(test_directory + ['-svv',
                          '--alluredir', allure_report_directory,
                          '--reruns', str(max_retries),  # 添加重试参数
                          '--reruns-delay', '1',  # 重试间隔1秒
                          ])
    if result == 0:

        print("所有用例全部执行通过，正在生成Allure HTML报告...")
        os.system(f'allure generate {allure_report_directory} -o {html_report_directory} --clean')

    elif result == 1:
        print("有用例实际结果与预期结果不符，正在生成Allure HTML报告...")
        os.system(f'allure generate {allure_report_directory} -o {html_report_directory} --clean')
    else:
        print("测试执行失败，请检查日志。")


if __name__ == '__main__':
    run_test()
