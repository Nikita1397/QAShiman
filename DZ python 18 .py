# Программа должна вывести: сколько раз символ встречается в строке, на какой позиции встречается первый раз.
stroka = input("Введите строку:")
simvol = input("Введите букву для проверки:")
def check(stroka, simvol):
    if not stroka:
        return 0
    elif stroka[0] == simvol:
        return 1 + check(stroka[1:], simvol)
    else:
        return check(stroka[1:], simvol)
pozicia = stroka.index(simvol)
print("Количество повторений в строке :")
print(check(stroka, simvol))
print("Первый раз появляется на ", pozicia+1, "месте")
# Конец программы вывод колличество повторений символа в строке
# Вывод на какой позиции встречается в первый раз










