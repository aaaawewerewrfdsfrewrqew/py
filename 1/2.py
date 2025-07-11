numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = len(numbers) - even_count

print("Кількість парних чисел:", even_count)
print("Кількість непарних чисел:", odd_count)
numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))

max_num = max(numbers)
min_num = min(numbers)

print("Максимальне значення:", max_num)
print("Мінімальне значення:", min_num)

import random

numbers = [random.randint(-10, 10) for _ in range(20)]
print("Список чисел:", numbers)

positive = [num for num in numbers if num > 0]
negative = [num for num in numbers if num < 0]
zeros = numbers.count(0)

min_positive = min(positive) if positive else None
max_negative = max(negative) if negative else None

print("Мінімальний додатний елемент:", min_positive)
print("Максимальний від'ємний елемент:", max_negative)
print("Кількість додатних елементів:", len(positive))
print("Кількість від'ємних елементів:", len(negative))
print("Кількість нулів:", zeros)

numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))
threshold = int(input("Введіть число: "))

filtered = [num for num in numbers if num >= threshold]
print("Результат:", filtered)

expression = input("Введіть арифметичний вираз (наприклад, 23+12): ")

if '+' in expression:
    parts = expression.split('+')
    result = int(parts[0]) + int(parts[1])
elif '-' in expression:
    parts = expression.split('-')
    result = int(parts[0]) - int(parts[1])
elif '*' in expression:
    parts = expression.split('*')
    result = int(parts[0]) * int(parts[1])
elif '/' in expression:
    parts = expression.split('/')
    if int(parts[1]) != 0:
        result = int(parts[0]) / int(parts[1])
    else:
        result = "Ділення на нуль!"
else:
    result = "Неправильний вираз."

print("Результат:", result)

numbers = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))
neg_indices = [i for i, num in enumerate(numbers) if num < 0]
non_negatives = sorted([num for num in numbers if num >= 0])

result = []
j = 0
for i in range(len(numbers)):
    if i in neg_indices:
        result.append(numbers[i])
    else:
        result.append(non_negatives[j])
        j += 1

print("Результат:", result)