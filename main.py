
# 1. Average
def average(a, b, c):
    result = (a + b + c) / 3
    return round(result, 2)


# 2. Even + >10
def foo(something) -> bool:
    return something % 2 == 0 and something > 10


# 3. Vowels
def count_vowels(text: str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# ---- тесты (это для фото) ----

print(average(3, 6, 9))
print(foo(12))
print(foo(8))
print(count_vowels("Hello World"))