
# ЗАВДАННЯ 1


numbers = [1, 5, 2, 8, 3, 7]

max_number = max(numbers)
min_number = min(numbers)
sum_numbers = sum(numbers)

print("Завдання 1")
print("Список:", numbers)
print("Найбільше число:", max_number)
print("Найменше число:", min_number)
print("Сума всіх чисел:", sum_numbers)

print("\n------------------------\n")


#ЗАВДАННЯ 2


grades = [10, 8, 12, 7, 9]

average = sum(grades) / len(grades)

above_average = []

for grade in grades:
    if grade > average:
        above_average.append(grade)

print("Завдання 2")
print("Оцінки:", grades)
print("Середній бал:", round(average, 2))
print("Оцінки вище середнього:", above_average)