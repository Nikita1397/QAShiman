# Программа, в которой реаизовано две функции
# Первый  – встроенным методом Питон sort()
# Второй - сортирует список целых чисел "пузырьком"
spisok = []
chislo = input("Введите числа : ")
for a in chislo:
    if a != " ":
        spisok.append(a)
def sort(spisok):
    spisok.sort()
    print(" Метод Питон:", spisok)
def puzirek(spisok):
    sort_on = True
    while sort_on:
        sort_on = False
        for a in range(len(spisok)-1):
            if int(spisok[a]) > int(spisok[a+1]):
                spisok[a], spisok[a+1] = spisok[a+1], spisok[a]
                sort_on = True
    print(" Метод пузырька:", spisok)
puzirek(spisok)
sort(spisok)
