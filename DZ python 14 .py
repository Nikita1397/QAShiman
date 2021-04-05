# Два списка заполняются целыми случайными числами, по 20 в каждом.
import random
# Делаем списки
Diapason1 = []
Diapason2 = []
spisok1 = [] #содержит элементы обоих списков
spisok2 = [] #содержит элементы обоих списков без повторений;
spisok3 = [] #содержит элементы общие для двух списков;
spisok4 = [] #содержит только уникальные элементы каждого из списков;
spisok5 = [] #содержит только минимальное и максимальное значение каждого из списков
# Выборка чисел
for a in range(20):
    b = random.randint(0, 50)
    Diapason1.append(b)
    c = random.randint(0, 50)
    Diapason2.append(c)
# Условия spisok1 и spisok2
spisok1 = Diapason1 + Diapason2
spisok2 = list(set(spisok1))
# Условия spisok3 и spisok4
for a in Diapason1:
    if a in Diapason2:
        spisok3.append(a)
    else:
        spisok4.append(a)
for b in Diapason2:
    if b not in Diapason1:
        spisok4.append(b)
# Условия для  spisok5
list.sort(Diapason1)
list.sort(Diapason2)
min1 = Diapason1[0]
max1 = Diapason1[-1]
min2 = Diapason2[0]
max2 = Diapason2[-1]
spisok5 = min1, max1, min2, max2
print(Diapason1)
print(Diapason2)
print("Список с элементами обоих списков: ", spisok1)
print("Список с элементами обоих списков без повторений: ", spisok2)
print("Список с элементами общими для двух списков: ", spisok3)
print("Список с уникальными элементами каждого из списков: ", spisok4)
print("Список с минимальными и максимальными значениями: ", spisok5)