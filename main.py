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

text = input("Введіть текст: ")


sentences = []
sentence = ""
for ch in text:
    sentence += ch
    if ch == '.':
        sentence = sentence.strip()
        if len(sentence) > 0:
            sentence = sentence[0].upper() + sentence[1:]
        sentences.append(sentence)
        sentence = ""


if sentence.strip() != "":
    sentence = sentence.strip()
    sentence = sentence[0].upper() + sentence[1:]
    sentences.append(sentence)

new_text = ' '.join(sentences)
print(new_text)


digit_count = 0
for ch in text:
    if ch in "0123456789":
        digit_count += 1


punctuation_count = 0
punctuation = [',', '.', ';', ':', '!', '?', '-', '—', '(', ')']
for ch in text:
    for mark in punctuation:
        if ch == mark:
            punctuation_count += 1


exclamation_count = 0
for ch in text:
    if ch == '!':
        exclamation_count += 1

print("\nКількість цифр:", digit_count)
print("Кількість розділових знаків:", punctuation_count)
print("Кількість знаків оклику:", exclamation_count)

#6

numbers = input("Введіть список цілих чисел через пробіл: ").split()
numbers = [int(x) for x in numbers]

for num in numbers[:]:
    if numbers.count(num) > 1:
        while num in numbers:
            numbers.remove(num)

print("Список без повторюваних чисел:", numbers)
