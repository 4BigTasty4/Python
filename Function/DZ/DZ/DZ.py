#1. Напишите функцию, которая принимает два числа 
#в качестве параметра и отображает все нечетные числа 
#между ними.

print("Hello User")
def MyPram(number, num):
    for f in range(number, num + 1):
        if f % 2 != 0:
            print(f)
number = int(input("Input Number: "))
num = int(input("Input Number 2: "))

MyPram(number, num)     

#2. Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа. 
#Функция принимает в качестве параметра: длину линии, 
#направление, символ.


print("Hello User")
def MyGorizontVertical(leght, direction, symbol):
    for u in range(1,leght+1):
        if direction == 1:
            print(symbol)
        elif direction == -1:
            print(symbol * leght)
            leght -= leght + 1



leght = int(input("input leght: "))
direction = int(input("input direction 1 or -1: "))
symbol = input("input synbol: ")
MyGorizontVertical(leght, direction, symbol)


#3. Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве 
#параметров


print("Hello User")
def MyDiapazon(number, number1, number2, number3):
    if number > number1 and number > number2 and number > number3:
        print(number)
    elif number1 > number and number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number and number2 > number1 and number2 > number3:
        print(number2)
    elif number3 > number and number3 > number1 and number3 > number2:
        print(number3)

number = int(input("Input Number: "))
number1 = int(input("Input Number1: "))
number2 = int(input("Input Number2: "))
number3 = int(input("Input Number3: "))

MyDiapazon(number, number1, number2, number3)

#4. Напишите функцию, которая возвращает сумму чисел 
#в указанном диапазоне. Границы диапазона передаются 
#в качестве параметров.


print("Hello User")
def MyDiapazon(number, num):
    for r in range(number, num):
        number += (r + 1) 
    print(number) 

        
number = int(input("Iput Number: "))
num = int(input("Iput Number: "))
MyDiapazon(number, num)
