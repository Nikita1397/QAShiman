# Программа замены слова в строке
Stroka = input("Введите строку: ")
Slovo = input("Введите слово для поиска: ")
Zam = input("Введите слово для замены: ")
# Поиск слова в строке и замена его
for a in range(len(Stroka) - len(Slovo)+1):
    if Slovo == Stroka[a:a + len(Slovo)]:
        stroka = Stroka.replace(Slovo, Zam)
print(Stroka)
# Конец программы вывод строки с заменныным словом

