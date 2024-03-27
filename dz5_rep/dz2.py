def is_float(string):
    try:
        float_number = float(string)
        return True
    except ValueError:
        return False

def generator_numbers(text: str):
    def generator():
        res = text.split()
        for i in res:
            if is_float(i):
                yield float(i)

    return generator()


def sum_profit(text: str, func):
    result = 0
    generator = func(text)
    for i in generator:
        result += i
    return result


x = """"Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""

print(sum_profit(x, generator_numbers))
