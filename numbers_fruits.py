
# задание 1


numbers = [3, 7, 2, 9, 4, 6, 1, 8]

# парні числа
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# подвоєні парні
doubled_even = []

for num in even_numbers:
    doubled_even.append(num * 2)

# перевірка та видалення 8
if 8 in doubled_even:
    doubled_even.remove(8)

print("Завдання 1")
print("Парні числа:", even_numbers)
print("Подвоєні парні:", doubled_even)

print("\n------------------------\n")


# задание 2


words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]

# унікальні слова
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

# слова довші 4 символів
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

# верхній регістр
upper_words = []

for word in long_words:
    upper_words.append(word.upper())

# перевірка BANANA
if "BANANA" in upper_words:
    print("BANANA є у списку")

print("Завдання 2")
print("Унікальні слова:", unique_words)
print("Довгі слова:", long_words)
print("Верхній регістр:", upper_words)