# Задача1
# Программа для проверки кратности диапозона
Start = int(input("Введите начало диапозона"))
End = int(input("Введите конец диапозона"))
# Вывод на экран чисел диапозона кратных 7
for i in range(Start, End):
    if i % 7 == 0:
        print(i, end=', ')
print("Все числа диапозона,кратные 7")
# Конец программы

# Задача 2
#Программа анализа чисел диапозона
Start = int(input("Введите начало диапозона"))
End = int(input("Введите конец диапозона"))
# Вывод на экран всех чисел диапозона
for i in range(Start, End+1):
 print(i, end=', ')
print("Все цифры диапозна")
# Вывод на экран всех чисел диапозона в обратном порядке
for i in range(End, Start-1, -1):
        print(i, end=' ,')
print("Все числа диапазона в убывающем порядке")
# Вывод на экран чисел диапозона кратных 7
for i in range(Start, End):
    if i % 7 == 0:
        print(i, end=', ')
print("Все числа диапозона,кратные 7")
# Вывод на экран чисел диапозона кратных 5
for i in range(Start, End):
  if i % 5 == 0:
    print(i, end=', ')
print("Все числа диапозона,кратные 5")
# Конец программы


# Задача 3 
# Программа анализа чисел диапозона
Start = int(input("Введите начало диапозона"))
End = int(input("Введите конец диапозона"))
     #Если число кратно 3 и 5 нужно вывести Fizz Buzz
for i in range(Start, End+1):
     if i % 3 == 0 and i % 5 == 0:
         print("Fizz Buzz")
     # Если число кратно 3 нужно вывоводится слово Fizz
     elif i % 3 == 0:
           print("Fizz")
     #Если число кратно 5 нужно выводится слово Buzz
     elif i % 5 == 0:
         print("Buzz")
     # Если число не кратно не 3 и 5  выводится само число указанного диапозона.
     else :
         print(i)
     # Конец программы







