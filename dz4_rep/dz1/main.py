def total_salary(path: str) -> tuple:
    with open(path, "r", encoding="utf-8") as file:
        line = file.read().replace("\n", ",")

    line = line.split(",")
    result = 0
    count = 0
    for i in line:
        if i.isdigit():
            result += int(i)
            count += 1
    return result, int(result / count)


if __name__ == '__main__':
    assert total_salary("asd.txt") == (6000, 2000)
    x, y = total_salary("asd.txt")
    print(f'Загальна сума заробітної плати: {x}, Середня заробітна плата: {y}')