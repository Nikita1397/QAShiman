# Начало программы
a1 = int(input("Введите первое число"))
b1 = int(input("Введите второе число"))
Summa = 0
Summa1 = 0
Summa2 = 0
for i in range(a1, b1+1):
#Расчет суммы нечетных чисел
    if i % 2 != 0:
        Summa += i
# Расчет суммы четных чисел
    if i % 2 == 0:
        Summa1 += i
# Расчет суммы кратных 9 чисел
    if i % 9 == 0:
        Summa2 += i
print("Сумма нечетных: ", Summa)
print("Сумма четных: ", Summa1)
print("Сумма кратных на 9: ", Summa2)
# Конец программы




# Начало программы
n = int(input("Введите число"))
# Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
while n !=7:
#  Если число больше нуля нужно вывести надпись "Number is positive"
 if n > 0:
       print("Number is positive")
#  Если меньше нуля «Number is negative»
 elif n < 0:
      print("Number is negative")
# Если равно нулю «Number is equal to zero»
 elif n == 0:
    print("Number is equal to zero")

 n = int(input("Введите число"))
 break
print("«Good bye!»")
# Конец программы

