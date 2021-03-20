# Показать на экран все простые числа в диапазоне, указанном пользователем
A= int(input("Первое число диапозона"))
B = int(input("Второе число диапозона"))
for i in range(A, B + 1):

   flag = True

   for f in range(2, i):

    if i % f == 0:

           flag = False

           break

   if flag:
       print(i, end= ',')
# Вывод простых чисел


# Показать на экран таблицу умножения в диапазоне, указанном пользователем.
a = int(input("Первое число "))
b = int(input("Второе число "))

for i in range(a,  b+1):
       for j in range(1, 11):
        print(i, "*", j, "=",  i*j, end=',')
# Конец программы




