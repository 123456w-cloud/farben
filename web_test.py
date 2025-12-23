# # test_example.py
# import pytest
#
# def test_example():
#     assert 1 + 1 == 2
#
# # if __name__ == '__main__':
# #     print("直接运行文件...")
# #     pytest.main([__file__, "-v"])  # 可能显示空套件
import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com")
    driver.maximize_window()
    yield driver
    sleep(5)
    driver.quit()


#
# class Testdoyin:
#     def test_web(self, setup):
#         setup.find_element(By.ID, "q").send_keys("123456")


# # 方案一：使用类（需要调整fixture使用方式）
# class TestDouyin:
#     @pytest.fixture(autouse=True)
#     def setup_class(self, setup):
#         self.driver = setup
#
#     def test_web(self):
#         self.driver.find_element(By.ID, "q").send_keys("123456")
#
#
# # 方案二：直接使用函数（推荐，更简单）
# def test_web_simple(setup):
#     setup.find_element(By.ID, "q").send_keys("123456")

def test_web(setup):
    setup.find_element(By.ID, "q").send_keys("123456")

    # 先点击页面主体确保获得焦点
    body = setup.find_element(By.TAG_NAME, "body")
    body.click()
    time.sleep(1)

    # 创建 ActionChains 对象
    actions = ActionChains(setup)

    # 1. 使用 PAGE_DOWN/PAGE_UP 键滚动
    # actions.send_keys(Keys.PAGE_DOWN).perform()
    # time.sleep(3)
    # actions.send_keys(Keys.PAGE_UP).perform()
    # time.sleep(1)

    # 2. 使用方向键滚动
    actions.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    actions.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)

    # 3. 组合键快速滚动
    # for _ in range(5):
    #     actions.send_keys(Keys.PAGE_DOWN).perform()
    #     time.sleep(0.3)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com")
    driver.maximize_window()
    yield driver
    sleep(5)
    driver.quit()


def test_reliable_scroll(driver):
    """可靠的滚动方法"""
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    for _ in range(3):
        # 方法1：先点击再按键

        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.3)

        # # 方法2：直接发送到body元素（更可靠）
        # body.send_keys(Keys.PAGE_DOWN)
        # time.sleep(0.3)
