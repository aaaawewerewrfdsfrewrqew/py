#1

list1 = input("введіть список чисел: ").split()
num = 0
for i in range(len(list1)):
    num += 1
suma = 0
for i in range(len(list1)):
    suma += int(list1[i])
s = suma / num
print("Кількість чисел:", num)
print("Середнє арифметичне:", s)

#2

list2 = input("введіть список чисел: ").split()
number = int(input("введіть число для пошуку: "))
n2 = 0
for i in range(len(list2)):
    if int(list2[i]) == number:
        n2 += 1

print("Кількість числа", number, "в списку:", n2)

#3

list3 = input("введіть список чисел: ").split()
suma2 = 0

for num in list3:
    if int(num) > 0:
        suma2 += int(num)

print("Сума додатніх чисел: ", suma2)

#4

list4 = input("введіть список чисел: ").split()
indexlist = []
for i in range(len(list4)):
    if int(list4[i]) % 2 == 0:
        indexlist.append(i)
print("Індекси парних чисел:", indexlist)

#5

sting = input("введіть рядок: ").split()

number_count = 0
rozdil_count = 0
symbol_count = 0


upper = sting.title()

for i in range(len(sting)):
    if sting[i].isdigit():
        number_count += 1
    elif sting[i] == "," or "." or ";" or ":" or "?":
        rozdil_count += 1
    elif sting[i] == "!":
        symbol_count += 1

print(upper)
print("кількість чисел:", number_count)
print("кількість розділових знаків:", rozdil_count)
print("кількість символів '!' :", symbol_count)

#6

numbers = input("Введіть список цілих чисел через пробіл: ").split()
numbers = [int(x) for x in numbers]

for num in numbers[:]:
    if numbers.count(num) > 1:
        while num in numbers:
            numbers.remove(num)

print("Список без повторюваних чисел:", numbers)