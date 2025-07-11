import random

#1

input_string = input("Введіть список цілих чисел, розділених пробілами: ").split()
count = 0
for i in range(len(input_string) - 1):
    if int(input_string[i]) < int(input_string[i + 1]):
        count += 1
                
print("Кількість чисел, які більші за попереднє: ", count)

#2

list_input = input("Введіть список чисел через пробіл: ").split()

numbers = [int(x) for x in list_input]

for num in numbers:
    if numbers.count(num) == 1:
        print(num, end=' ')

#3

list_input = input("Введіть список чисел через пробіл: ").split()


numbers = [int(x) for x in list_input]

max_seq = []        
current_seq = []    

for i in range(len(numbers)):
    if i == 0 or numbers[i] > numbers[i - 1]:
        current_seq.append(numbers[i])
    else:
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
        current_seq = [numbers[i]]

if len(current_seq) > len(max_seq):
    max_seq = current_seq

print("Довжина послідовності:", len(max_seq))
print("Послідовність:", max_seq)

#4

list_input = input("Введіть список чисел через пробіл: ").split()
numbers = [int(x) for x in list_input]
n = int(input("Число позицій N: "))
n = n % len(numbers)
shifted = numbers[-n:] + numbers[:-n]
print("Зсунутий список:", shifted)

#5

list1 = [random.randint(1, 20) for а in range(10)]
list2 = [random.randint(1, 20) for а in range(10)]

print("cписок 1:", list1)
print("cписок 2:", list2)
combined = list1 + list2
print("\n Об'єднаний список:", combined)
combined_no_duplicates = list(set(combined))
print("Об'єднаний без повторень:", combined_no_duplicates)

common_elements = list(set(list1) & set(list2))
print("3. Спільні елементи:", common_elements)
unique_elements = list(set(list1) ^ set(list2))
print("унікальні елементи кожного списку:", unique_elements)
min_max_list = [min(list1), max(list1), min(list2), max(list2)]
print("мінімальне і максимальне значення кожного списку:", min_max_list)

#6

list_input = input("Введіть список чисел через пробіл: ").split()
numbers = [int(x) for x in list_input]
numbers.sort()
result = []
left = 0
right = len(numbers) - 1
while left <= right:
    result.append(numbers[left])
    left += 1
    if left <= right:
        result.append(numbers[right])
        right -= 1
print("Результат:", result)

