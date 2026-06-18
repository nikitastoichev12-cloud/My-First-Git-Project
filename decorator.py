def check_integer_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, int):
            return result + 10

        return result

    return wrapper


@check_integer_result
def sum_numbers(a, b):
    return a + b


@check_integer_result
def divide_numbers(a, b):
    return a / b


print(sum_numbers(5, 3))      # 8 + 10 = 18
print(divide_numbers(5, 2))   # 2.5