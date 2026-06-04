from typing import Union


def calc(a: float, b: float, operation: str = "sum") -> float:
    if operation == "sub":
        return a - b
    return a + b



def change_text(text: str, upper: bool = True) -> str:
    if upper:
        return text.upper()
    return text.lower()



def sum_numbers(numbers: str, separator: str = ",") -> int:
    parts = numbers.split(separator)
    nums = [int(x.strip()) for x in parts]
    return sum(nums)