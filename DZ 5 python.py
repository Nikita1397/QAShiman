#Задача 1
#Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
#на экран сумму трёх чисел или произведение трёх чисел.

A = int(input("Введите число"))
B = int(input("Введите число"))
C = int(input("Введите число"))
D = (A+B+C)
E = (A*B*C)
Art = input() #  'Cумма' , 'Произведение'
if Art == 'Сумма':
    print(D)
if Art == 'Произведение ':
    print(E)



# Задача 2
# Пользователь вводит с клавиатуры количество метров.В зависимости от выбора пользователя программа переводит метры в
# мили, дюймы или ярды.

Metr = int(input("Введите количество метров "))
Api = input()  # 'мили' 'дюймы' 'ярды'

if Api == 'мили':
    print(Metr*0.000621371)
if Api == 'дюймы':
    print(Metr*39.3701)
if Api == 'ярды':
    print(Metr*1.09361)








