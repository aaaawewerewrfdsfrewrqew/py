text = "введіть ваш текст: "


temp_text = text.replace('!', '.').replace('?', '.')
sentences = temp_text.split('.')


sentences = [s.strip() for s in sentences if s.strip()]

print("Кількість речень:", len(sentences))

text = input("Введіть рядок: ")


cleaned = ''
for ch in text.lower():
    if ch.isalnum():
        cleaned += ch

if cleaned == cleaned[::-1]:
    print("Це паліндром.")
else:
    print("Це не паліндром.")
    
reserved_words = ['if', 'else', 'while', 'return']

text = input("Введіть текст: ")

words = text.split()

new_words = []
for word in words:

    stripped = word.strip('.,!?:;()[]{}"\'')
    if stripped.lower() in reserved_words:

        new_word = word.upper()
    else:
        new_word = word
    new_words.append(new_word)

result = ' '.join(new_words)
print("Змінений текст:")
print(result)

text = input("Введіть рядок: ")
char1 = input("Введіть перший символ: ")
char2 = input("Введіть другий символ: ")

start = text.find(char1)
end = text.find(char2)

if start != -1 and end != -1 and start <= end:
    result = text[:start] + text[end+1:]
else:
    result = text

print("Результат:")
print(result)

text = input("Введіть текст: ")
chars = input("Введіть символи: ")

words = text.split()

result_words = []
for word in words:

    has_char = False
    for c in chars:
        if c in word:
            has_char = True
            break
    if not has_char:
        result_words.append(word)

result = ' '.join(result_words)
print("Результат:")
print(result)

text = input("Введіть текст: ")

words = text.split()
reversed_words = []
for i in range(len(words)-1, -1, -1):
    reversed_words.append(words[i])

result = ' '.join(reversed_words)
print("Зворотний текст:")
print(result)