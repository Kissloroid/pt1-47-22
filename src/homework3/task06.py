"""
Во входной строке записан текст. Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки. Определите, сколько различных слов содержится в этом тексте.
"""


input_text = input('Введите текст: ').split(' ')
print(input_text)
print(set(input_text))
print(f'Количество разных слов в ведённом тексте: {len(set(input_text))}')