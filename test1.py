import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def driver():
    """创建浏览器驱动"""
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_reliable_scroll(driver):
    """可靠的滚动测试"""
    body = driver.find_element(By.TAG_NAME, "body")

    # 向下滚动3次
    for i in range(3):
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.3)
        print(f"向下滚动第{i + 1}次")

    # 可以添加断言
    assert "淘宝" in driver.title


# 不要在这里直接调用测试函数！
# 让pytest自动发现和执行测试函数
if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])