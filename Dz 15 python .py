
#Напишите программу , которая отображает пустой или заполненный квадрат из некоторого символа.
Dlina1 = int(input("Введите длину стороны квадрата: "))
Simvol= input("Введите символ квдрата : ")
Poln = input("Введите заполненность квадрата , 1 - если квадрат заполненный, 2 - если пустой: ")
# Вводим переменную логического типа
if Poln == "1":
    Pol = True
else:
    Pol = False
# Вводим функцию
def kvadrat (Dlina1,Simvol,Poln):
    if Poln:
        side = Simvol*Dlina1
    else:
        side = Simvol + " " * (Dlina1-2)+Simvol
    print(Simvol*Dlina1)
    for a in range(Dlina1-2):
        print(side)
    print(Simvol*Dlina1)
kvadrat (Dlina1, Simvol, Pol)
# Конец программы вывод квадрата

#Напишите программу, которая считает количество цифр в числе.
Chislo = input("Введите число: ")
def dlina(Chislo):
    print(len(Chislo))
dlina(Chislo)
# Конец программы вывод колличество цифр в числе 
