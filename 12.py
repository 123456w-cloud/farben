from itertools import combinations


def count_lines(filename):
    try:
        with open(filename, encoding="utf-8") as file:
            count = 0
            for line in file:
                if line.strip() and not line.strip().startswith("#"):
                    count += 1
            return count
    except Exception as e:
        print(f"错误：{e}")
        return -1


print(count_lines("web_test.py"))


def dangerous_code():
    for comb in combinations(range(1, 101), 8):
        if sum(comb) == 100:
            print(comb)
            break


dangerous_code()
