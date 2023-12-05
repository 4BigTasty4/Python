# 2 Создать функцию, которая будет отображать трегольник выбранным символом

#     $
#    $$$
#   $$$$$
#  $$$$$$$
# $$$$$$$$$



print("Hello User")
symbol = str(input("Input Symbol: "))
number = int(input("Input Your Range: "))
def Mysymbol():
    global number, symbol
    for u in range(0,number + number):
       if u % 2 != 0:
           print(" " * number, symbol * u)
           number -= 1


Mysymbol()



#3 Создать функцию, которая высчитывает эквивалент введённой пользователем суммы по выбронной валюте


print("Hello User")
money = float(input("Input Money: "))
vallue = str(input("Input Kurs: "))

usd = 1.7
euro = 1.79
tl = 0.11

def Myvalue():
    global valluye, usd, euro, tl
    if vallue == "usd" and "USD" and "Usd":
        print(money * usd)
    elif vallue == "euro" and "Euro" and "EURO":
        print(money * euro)
    elif vallue == "tl" and "Tl" and "TL":
        print(money * tl)
    else:
        print("Error")

Myvalue()




# 4 Создать функцию, которая будет проверять введённый пользователем логин и пароль до тех пор, пока данные не будут введены верно с помощью цикла


print("Hello User")
wifiName = "qwerty"
wifiPasword = "qwerty123"        

def Wifi():
    global wifiName, wifiPasword
    while True:
        wifi = input("Input Wifi Name: ")
        pasword = input("Input Wifi Pasword: ")
        if wifi == wifiName and pasword == wifiPasword:
            print("Connect....")
            break
        else:
            print("Error")
            continue


Wifi()


# 5 Создать функцию, которая будет проверять введённый пользователем логин и пароль до тех пор, пока данные не будут введены верно с помощью рекурсии

print("Hello User")
login = "Angry"
pasword = "Angry333"
def Login():
    while True:
        userLogin = input("Input Login: ")
        userPasword = input("Input Pasword: ")
        if login == userLogin and pasword == userPasword:
            print("Succses")
            break
        else:
            print("Error")
            Login()

Login()