#Задача 1
#	Нужно написать программу, которая будет
#- принимать от пользователя несколько профессий
#- принимать от пользователя, чем их разделить
#и выводить следующие сообщение:


a = input("Введите профессию")
b = input("Введите вторую профессию")
c = input("Введите третью профессию")

print(a)
print(b)
print(c)


print("Кто он?")
print((("Он -")+((a)+(" ")+("и")+(" ")+(b)+(" ")+("и")+(" ")+(c))))

#Задача 2
#Нужно написать программу, которая будет принимать от пользователя количество минут, а выводить сколько это часов и сколько минут.

print("Программа перевода минут в часы и остаток минут")
time = int(input("введите число"))
hours = (time // 60)
Min = time % 60
print(hours, "Часов"+str(Min), "Минут ")

