# задача 1
# Распределение цифр по условиям
Chislo = int(input("Вводим число от 1 до 100"))
# Если число кратно 3 и 5 нужно вывести Fizz Buzz.
if Chislo % 3 == 0 and Chislo % 5 == 0:
    print('FizzBuzz')
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz
elif Chislo % 3 == 0:
    print('Fizz')
# Если число кратно 5 нужно вывести слово Buzz
elif Chislo % 5 == 0:
    print('Buzz')
# Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.
elif Chislo <= 0:
    print('Error')
elif Chislo >= 100:
    print('Error')
# Если число не кратно не 3 и 5 нужно вывести само число
else:
    print(Chislo)
# Конец программы

# Задача 3 Определение времени года по номеру месяца
a = int(input('Choose a month'))
# Winter (если введено значение 1,2 или 12)
if a == 1 or a == 2 or a == 12:
    print('Winter')
# Spring (если введено значение от 3 до 5)
elif a == 3 or a == 4 or a == 5:
    print('Sping')
# Summer (если введено значение от 6 до 8)
elif a == 6 or a == 7 or a == 8:
    print('Summer')
# Autumn (если введено значение от 9 до 11).
elif a == 9 or a == 10 or a == 11:
    print('Autumn')
# Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке
else:
    print('Error')
# Итог программы вывод времени года по введенному номеру
