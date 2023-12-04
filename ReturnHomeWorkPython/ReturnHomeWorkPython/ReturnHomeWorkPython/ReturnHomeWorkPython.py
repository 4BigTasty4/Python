#                                                    8.04.2022 


# N 1

#print("Hello User")

#height = int(input("Enter Your Height in Centimeteres: "))

#resultM = height // 100
#resultCM = height % 100

#print(f"You Are {resultM} M And {resultCM} CM")



# N 2

#print("Hello User")

#moneySum = int(input("Enter The Amount Of Money: "))

#moneyKurs = float(input("Select The Exchange Rate: "))

#result = moneySum * moneyKurs

#print(f"Your Money: {result}")



# N 3

#print("Hello User")

#word = input("Input Word: ")

#number = int(input("Input Number To Repit: "))

#result = word * (number % 10)

#print(result)


#                                                    15.04.2022 


#print("Hello User")

#var = 1

#if var != str(var) and var != bool(var) and var != float(var):
#    if var == int(var):
#        print("It Is Integeer")
#else:
#    print("It Is Not Integeer")



#print("Hello User")

#visa = str(input("Input Visa: "))
#wallet = float(input("Input Money: "))

#if wallet >= 40000:
#    if visa == "yes" or visa == "Yes" or visa == "YES":
#        print("Go To USA")
#    else:
#        print("Go Home")
#else:
#    print("Go Home")



#print("Hello User")

#usd = 1.7
#tl = 0.9
#rub = 0.3

#money = float(input("Input Your Money: "))
#moneyKurs = int(input("Input Kurs (1 - USD ; 2 - TL ; 3 - RUB): "))

#if moneyKurs == 1:
#    result = money * usd
#    print(f"Your Money: {result}")
#elif moneyKurs == 2:
#    result = money * tl
#    print(f"Your Money: {result}")
#elif moneyKurs == 3:
#    result = money * rub
#    print(f"Your Money: {result}")
#else:
#    print("ERROR")


#                                                     18.04.2022 



#print("Hello User\n")

#name = str(input("Input Your Name: "))
#surname = str(input("Input Your Surname: "))

#bank = 0

#number1 = "A"
#number2 = "B"
#number3 = "C"
#number4 = "D"

#print(f"\nWelcome To Millionaire Game {name} {surname}\n")

#print("Victory table")
#print("Big Win - 50000$")

#print("\n")

#print("N1 2 + 2 = ?\n\nA)3 B)4 C)0 D)5\n")

#answer = str(input("Your Answer: "))

#if answer == number2:
#    bank += 10000
#    print(f"Correct\n")
#    if answer == number2:
#        print("N2 2 * 2 = ?\n\nA)4 B)3 C)0 D)5\n")
#        answer = str(input("Your Answer: "))
#        if answer == number1:
#            bank += 10000
#            print(f"Correct\n")
#            if answer == number1:
#                 print("N3 0 + (1 + 1) = ?\n\nA)4 B)5 C)0 D)3\n")
#                 answer = str(input("Your Answer: "))
#                 if answer == number4:
#                     bank += 10000
#                     print(f"Correct\n")
#                     if answer == number4:
#                        print("N4  5 + 5 = ?\n\nA)4 B)3 C)10 D)15\n")
#                        answer = str(input("Your Answer: "))
#                        if answer == number3:
#                            bank += 10000
#                            print(f"Correct\n")
#                            if answer == number3:
#                                print("N5  5 * 5 = ?\n\nA)4 B)25 C)10 D)20\n")
#                                answer = str(input("Your Answer: "))
#                                if answer == number2:
#                                    bank += 10000
#                                    print(f"Correct\n")
#                                    if answer == number2:
#                                        print(f"You Win And Your Bank {bank}")
#                                else:
#                                    print(f"Game Over And Your Bank: {bank}")
#                        else:
#                            print(f"Game Over And Your Bank: {bank}")
#                 else:
#                     print(f"Game Over And Your Bank: {bank}")
#        else:
#            print(f"Game Over And Your Bank: {bank}")
#else:
#    print(f"Game Over And Your Bank: {bank}")



#                                                     22.04.2022 



#                                                     Only Teory



#                                                     25.04.2022 


# input:    10
# ouptut:   9 6 3 

# input:    -10
# ouptut:   -9 -6 -3 

#number = int(input("Input Number: "))

#while True:

#    if number > 0:

#        number -= 1

#        if (number % 3) != 0:
#            continue

#        print(number)

#        if number == 0:
#            break;

#    if number < 0:
        
#        number += 1

#        if (number % 3) != 0:
#            continue

#        print(number)

#        if number == 0:
#            break;


#N 1

#print("Hello User")

#number = int(input("Input Number: "))
#power = int(input("Input Power: "))

#while True:
#    if power > 0:
#        result = number ** power
#        print(result)
#        break
#    if power < 0:
#        print("ERROR")
#        break
        
#print("Hello User")

#number = int(input("Input Number: "))
#power = int(input("Input Power: "))

#result = 1

#while power > 0:
#    result *= number
#    power -= 1

#if power >= 0:
#    print(result)
#else:
#    print("ERROR")


# N 2

#print("Hello User")

#number = int(input("Input Number To Factorial Calculation: "))

#numberAssistant = 1

#while True:
#    if number > 0:
#        numberAssistant *= number
#        number -= 1

#    if number == 0:
#        print(numberAssistant)
#        break


# N 3

#print("Hello User")

#number = int(input("Input Number: "))

#while True:

#    if number / 2 != 0

    


#                                                      29.04.2022



#                                                      06.05.2022


# Milionare Game

import random

bank = 0

fiftyfifty = True

isCorrect = True

question1 = "1 + 0 = ?"
variant1A = "A) 0"
variant1B = "B) 10"
variant1C = "C) -1"
variant1D = "D) 1"
correctAnswerQuestion1 = variant1D

question2 = "0 - 1 = ?"
variant2A = "A) -0"
variant2B = "B) 1"
variant2C = "C) -1"
variant2D = "D) !1"
correctAnswerQuestion2 = variant2B

question3 = "2 + 2 = ?"
variant3A = "A) 4"
variant3B = "B) !2"
variant3C = "C) 5"
variant3D = "D) 0"
correctAnswerQuestion3 = variant3C

print("Hello User Welocome To Milionaire Game \n")

print("Victory table")
print("3-rd. question - 10000$")
print("2-nd. question - 5000$")
print("1-st. question - 1000$")

print("\n")


# Question 1


if isCorrect:

    print("1. " + question1)
    print(variant1A)
    print(variant1B)
    print(variant1C)
    print(variant1D)

    print("\n")

    if fiftyfifty:
        print("Also you can press: ")
        print("1 to '50/50'")

    answer = input("Choose Your Variant: ")

    # 50/50

    if answer == "1" and fiftyfifty:
        fiftyfifty = False
        inCorrectAnswer = random.randint(1,3)
        isCorrectFirst = random.randint(0,1)

        if isCorrectFirst:
            print(correctAnswerQuestion1)

            if inCorrectAnswer == 1:
                print(variant1A)
            elif inCorrectAnswer == 2:
                print(variant1B)
            elif inCorrectAnswer == 3:
                print(variant1C)


        if not(isCorrectFirst):

            if inCorrectAnswer == 1:
                print(variant1A)
            elif inCorrectAnswer == 2:
                print(variant1B)
            elif inCorrectAnswer == 3:
                print(variant1C)

            print(correctAnswerQuestion1)

        answer = input("Choose Your Variant: ")


    isCorrect = answer == "D" or answer == "d"
    if isCorrect:
        bank += 1000



# Question 2


if isCorrect:

    print("2. " + question2)
    print(variant2A)
    print(variant2B)
    print(variant2C)
    print(variant2D)

    print("\n")

    if fiftyfifty:
        print("Also you can press: ")
        print("1 to '50/50'")

    answer = input("Choose Your Variant: ")

    # 50/50

    if answer == "1" and fiftyfifty:
        fiftyfifty = False
        inCorrectAnswer = random.randint(1,3)
        isCorrectFirst = random.randint(0,1)

        if isCorrectFirst:
            print(correctAnswerQuestion2)

            if inCorrectAnswer == 1:
                print(variant2A)
            elif inCorrectAnswer == 2:
                print(variant2C)
            elif inCorrectAnswer == 3:
                print(variant2D)


        if not(isCorrectFirst):

            if inCorrectAnswer == 1:
                print(variant2A)
            elif inCorrectAnswer == 2:
                print(variant2C)
            elif inCorrectAnswer == 3:
                print(variant2D)

            print(correctAnswerQuestion2)

        answer = input("Choose Your Variant: ")


    isCorrect = answer == "B" or answer == "B"
    if isCorrect:
        bank += 4000


# Question 3


if isCorrect:

    print("3. " + question3)
    print(variant3A)
    print(variant3B)
    print(variant3C)
    print(variant3D)

    print("\n")

    if fiftyfifty:
        print("Also you can press: ")
        print("1 to '50/50'")

    answer = input("Choose Your Variant: ")

    # 50/50

    if answer == "1" and fiftyfifty:
        fiftyfifty = False
        inCorrectAnswer = random.randint(1,3)
        isCorrectFirst = random.randint(0,1)

        if isCorrectFirst:
            print(correctAnswerQuestion3)

            if inCorrectAnswer == 1:
                print(variant2A)
            elif inCorrectAnswer == 2:
                print(variant2B)
            elif inCorrectAnswer == 3:
                print(variant2D)


        if not(isCorrectFirst):

            if inCorrectAnswer == 1:
                print(variant2A)
            elif inCorrectAnswer == 2:
                print(variant2B)
            elif inCorrectAnswer == 3:
                print(variant2D)

            print(correctAnswerQuestion3)

        answer = input("Choose Your Variant: ")


    isCorrect = answer == "C" or answer == "c"
    if isCorrect:
        bank += 6000   
        

if isCorrect:
    print(f"You Won And Your Bank {bank}")
else:
    print(f"HAHAHA You Lose And Your Bank {bank}")




                                                   # 09.05.2022



# N 5

#def CheckInfo():
    
#    name = "Pixar"
#    pasword = "A113"

#    checkName = input("Login: ")
#    checkPasword = input("Pasword: ")

#    if checkName == name and checkPasword == pasword:
#        print("Succses")
#    else:
#        CheckInfo()

#CheckInfo()


# N 4

#def CheckInfo():

#    while True:

#        name = "Pixar"
#        pasword = "A113"

#        checkName = input("Login: ")
#        checkPasword = input("Pasword: ")

#        if checkName == name and checkPasword == pasword:
#            print("Succses")
#            break
#        else:
#            continue

#CheckInfo()


# N 3

#def Vallue():

#    global usd,tl,euro

#    euro = 1.77
#    usd = 1.7
#    tl = 0.091


#def ChangeVallue():

#    global result,money,moneyChanger

#    print(f"Euro: {euro}; Dollar: {usd}; Tl: {tl} \n")

#    money = float(input("Input Your Money: "))
#    moneyChanger = input("Input Money Kurs: ")

#    if moneyChanger == "Euro" or moneyChanger == "EURO" or moneyChanger == "euro":

#       result = money * euro

#       print(f"Your Money: {result}")

#    elif moneyChanger == "Usd" or moneyChanger == "usd" or moneyChanger == "USD":

#       result = money * usd

#       print(f"Your Money: {result}")
#    elif moneyChanger == "TL" or moneyChanger == "TL" or moneyChanger == "tl":

#       result = money * tl

#       print(f"Your Money: {result}")

#    else:
#        print("There Is No Such Exchange Rate")


#Vallue()
#ChangeVallue()

 


                                                     # 13.05.2022




# N 1

#def oddFunc(number1,number2):

#    for i in range(number1,number2):
#        if i % 2 != 0:
#            print(i)



#number1 = int(input("Input Number1: "))
#number2 = int(input("Input Number2: "))

#oddFunc(number1,number2)



# N 3


#def myBigNumber(number1,number2,number3,number4):

#    if number1 > number2 and number1 > number3 and number1 > number4:
#        print(f"Big Number is: {number1}")
#    elif number2 > number1 and number2 > number3 and number2 > number4:
#        print(f"Big Number is: {number2}")
#    if number3 > number2 and number3 > number1 and number3 > number4:
#        print(f"Big Number is: {number3}")
#    elif number4 > number2 and number4 > number3 and number4 > number1:
#        print(f"Big Number is: {number4}")



#number1 = int(input("Input Number1: "))
#number2 = int(input("Input Number2: "))
#number3 = int(input("Input Number3: "))
#number4 = int(input("Input Number4: "))


#myBigNumber(number1,number2,number3,number4)



# N 4


#def diapazonSum(begginDiapazon,endDiapazon):

#    for i in range(begginDiapazon,endDiapazon):
#        begginDiapazon += (i + 1)
#    print(begginDiapazon)
         


#begginDiapazon = int(input("Input Beggin Diapazon: "))
#endDiapazon = int(input("Input End Diapazon: "))


#diapazonSum(begginDiapazon,endDiapazon)


#def MyDirection(lenght,direction,symbol):

#    for i in range(1,lenght + 1):

#        if direction == "1":
#            print(symbol)
#        else:
#            print(lenght * symbol)




#lenght = int(input("Input Lenght: "))
#direction = int(input("Input Direction(1 - Horizontal; 0 - Vertical): "))
#symbol = input("Input Symbol: ")

#MyDirection(lenght,direction,symbol)


