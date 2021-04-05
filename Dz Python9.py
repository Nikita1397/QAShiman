#первая задача
#Пользователь вводит границы диапазона и число
Diapozon1 = int(input("Введите первую границу диапазона: "))
Diapozon2 = int(input("Введите вторую границу диапазона: "))
Chis = int(input("Введите число: "))
#Условие для выбранного диапазона
for a in range(Diapozon1, Diapozon2 + 1):
# Повторение условия если не выполнено
    while Chis > Diapozon2 or Chis < Diapozon1:
     Сhis = int(input("Введите число: "))
    if a == Chis:
     print("!", a, "!", end="")
    else:
     print(a, end="")
#Конец программы выделение нужного числа


