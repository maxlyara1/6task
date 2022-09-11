import numpy as np #использую numpy
print('Введите текст для анализа: ')
text = input().split(" ")
text1 = []
text2 = []
for i in text:
    i = i.lower()
    text1.append(i)
for i in text1:
    for j in text1:
        print(i, j)
        x = int(input("Оцените насколько подходят эти слова друг другу(0-100): "))
        if x > 80:
            text2.append('i'+'j')
print(text2)