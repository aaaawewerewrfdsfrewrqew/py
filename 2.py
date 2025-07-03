
print("Завдання 1")
text = input("Введіть числа через пробіл: ")
numbers = text.split()
even = 0
odd = 0
for n in numbers:
    n = int(n)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Парних чисел:", even)
print("Непарних чисел:", odd)

print("\nЗавдання 2")
text = input("Введіть числа через пробіл: ")
numbers = text.split()
min_value = int(numbers[0])
max_value = int(numbers[0])
for n in numbers:
    n = int(n)
    if n < min_value:
        min_value = n
    if n > max_value:
        max_value = n
print("Мінімальне число:", min_value)
print("Максимальне число:", max_value)

print("\nЗавдання 3")
numbers = [3, -7, 0, 2, -5, 0, 4, -9, 0, 6]
print("Список:", numbers)
min_positive = None
max_negative = None
positive_count = 0
negative_count = 0
zero_count = 0
for n in numbers:
    if n > 0:
        positive_count += 1
        if min_positive is None or n < min_positive:
            min_positive = n
    elif n < 0:
        negative_count += 1
        if max_negative is None or n > max_negative:
            max_negative = n
    else:
        zero_count += 1
print("Мінімальне додатнє:", min_positive)
print("Максимальне від’ємне:", max_negative)
print("Кількість додатних:", positive_count)
print("Кількість від’ємних:", negative_count)
print("Кількість нулів:", zero_count)


print("\nЗавдання 4")
text = input("Введіть числа через пробіл: ")
numbers = text.split()
limit = int(input("Введіть порогове число: "))
new_list = []
for n in numbers:
    n = int(n)
    if n >= limit:
        new_list.append(n)
print("Новий список:", new_list)


print("\nЗавдання 5")
expr = input("Введіть вираз: ")
if "+" in expr:
    parts = expr.split("+")
    a = int(parts[0])
    b = int(parts[1])
    print("Результат:", a + b)
elif "-" in expr:
    parts = expr.split("-")
    a = int(parts[0])
    b = int(parts[1])
    print("Результат:", a - b)
elif "*" in expr:
    parts = expr.split("*")
    a = int(parts[0])
    b = int(parts[1])
    print("Результат:", a * b)
elif "/" in expr:
    parts = expr.split("/")
    a = int(parts[0])
    b = int(parts[1])
    if b == 0:
        print("Ділення на нуль!")
    else:
        print("Результат:", a / b)
else:
    print("Невідомий вираз")


print("\nЗавдання 6")
text = input("Введіть числа через пробіл: ")
numbers = text.split()
original = []
positives = []

for n in numbers:
    num = int(n)
    original.append(num)
    if num >= 0:
        positives.append(num)

positives.sort()

result = []
j = 0
for num in original:
    if num < 0:
        result.append(num)
    else:
        result.append(positives[j])
        j += 1

print("Результат:", result)
