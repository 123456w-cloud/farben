def count_lines(filename):
    with open(filename, encoding="utf-8") as f:
        lines = [line for line in f if line.strip() and not line.strip().startswith("#")]
        print("列表推导式")
        return len(lines)


# print(count_lines("test1.py"))
def count_lines(filename):
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            if stripped and not stripped.startswith("#"):

                count += 1
    print("for循环")
    return count


# print(count_lines("test1.py")) 后面覆盖前面的
print(count_lines("web_test.py"))

from itertools import combinations

# 原问题：1-100选8个数和100（计算量太大）
# 改为：1-20选5个数和20（原理相同）
# print("从1-100选8个不重复数和为100:")
#
# solutions = []
# for comb in combinations(range(1, 101), 7):
#     if sum(comb) == 100:
#         solutions.append(comb)
#
# for i, sol in enumerate(solutions):
#     print(f"解{i + 1}: {sorted(sol)} = {sum(sol)}")
#
# print(f"共找到 {len(solutions)} 个解")

# 不要直接运行这个！会卡死！
def dangerous_code():
    for comb in combinations(range(0, 101), 8):
        if sum(comb) == 100:
            print(comb)  # 可能几小时甚至几天后才输出
            break


def computer_speed():
    """测试计算机速度"""
    import time
    start = time.time()

    # 测试简单循环速度
    count = 0
    for i in range(1000000):  # 100万次
        count += i

    elapsed = time.time() - start
    print(f"100万次加法用时: {elapsed:.4f}秒")
    print(f"速度: {1000000 / elapsed:,.0f} 次/秒")

    if elapsed < 0.1:
        print("⚡ 你的电脑很快！")
    else:
        print("🐢 速度一般")



if __name__ == '__main__':
    dangerous_code()
    computer_speed()