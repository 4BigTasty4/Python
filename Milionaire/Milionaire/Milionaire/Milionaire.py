

import random

bankomat = 0

isCorrect = True

#helpers

fiftyFifty = True
audience = True
call = True

# Question

question1 = "0 - 1 = ?"
question2 = "2 + 2 = ?"
question3 = "0 * 1 = ?"
question4 = "10 * 10 = ?"

# allQuestionVariants

var1A = "A) !1"
var1B = "B) 1"
var1C = "C) -1"
var1D = "D) 10"

var2A = "A) 4"
var2B = "B) 5"
var2C = "C) 1"
var2D = "D) -4"

var3A = "A) !1"
var3B = "B) 1"
var3C = "C) 10"
var3D = "D) 15"

var4A = "A) 1"
var4B = "B) 1000"
var4C = "C) 10"
var4D = "D) 100"

# allCorrectAnswers

correctAnswer1 = var1C # == "C" or "c"
correctAnswer2 = var2B # == "B" or "b"
correctAnswer3 = var3D # == "A" or "a"
correctAnswer4 = var4A # == "D" or "d"

# Familiarization

print("Hello User Welocome To Milionaire Game! \n")

name = input("Input Your Name: ")

print("\n")

print(f"{name} This is Victory Table:")

print("\n")

print("4 - th. question - 20000$")
print("3 - rd. question - 15000$")
print("2 - nd. question - 10000$")
print("1 - st. question - 5000$")

# Question1

print("\n")

print("1. " + question1)
print(var1A)
print(var1B)
print(var1C)
print(var1D)

print("\n")

if fiftyFifty:
    print("Also you can press: ")
    print("1 to 50/50")
if call:
    print("Also you can press: ")
    print("2 to Call")
if audience:
    print("Also you can press: ")
    print("3 to Audience")

print("\n")

answer = input("Input Your Answer: ")

if answer == "1" and fiftyFifty:

    fiftyFifty = False

    wrongAnswerFifty = random.randint(1, 3)
    correctAnswerFifty = random.randint(1, 2) == 1

    if correctAnswerFifty:

        print(correctAnswer1)

        if wrongAnswerFifty == 1:
            print(var1A)
        elif wrongAnswerFifty == 2:
            print(var1B)
        elif wrongAnswerFifty == 3:
            print(var1D)

    elif not(correctAnswerFifty):

        if wrongAnswerFifty == 1:
            print(var1A)
        elif wrongAnswerFifty == 2:
            print(var1B)
        elif wrongAnswerFifty == 3:
            print(var1D)

        print(correctAnswer1)

    answer = input("Input Your Answer: ")

elif answer == "2" and call:

        call = False

        enterCall1 = random.randint (1, 4)

        if enterCall1 == 1:
            print(f"Your friend chose: {var1A}")
        elif enterCall1 == 2:
            print(f"Your friend chose: {var1B}")
        elif enterCall1 == 3:
            print(f"Your friend chose: {var1C}")
        elif enterCall1 == 4:
            print(f"Your friend chose: {var1D}")

        answer = input("Input Your Answer: ")

elif answer == "3" and audience:

        audience = False

        audienceVarD = random.randint(0,30)
        audienceVarB = random.randint(0,30)
        audienceVarA = random.randint(0,30)
        audienceVarC = 100 - (audienceVarD + audienceVarB + audienceVarA)
        
        print(f"{var1A} = {audienceVarA}%")
        print(f"{var1B} = {audienceVarB}%")
        print(f"{var1C} = {audienceVarC}%")
        print(f"{var1D} = {audienceVarD}%")

        answer = input("Input Your Answer: ")


isCorrect = answer == "C" or answer == "c"


if isCorrect:
    bankomat += 5000


# Question 2


if isCorrect:

    print("\n")

    print("2. " + question2)
    print(var2A)
    print(var2B)
    print(var2C)
    print(var2D)
    
    print("\n")
    
    if fiftyFifty:
        print("Also you can press: ")
        print("1 to 50/50")
    if call:
        print("Also you can press: ")
        print("2 to Call")
    if audience:
        print("Also you can press: ")
        print("3 to Audience")
    
    print("\n")
    
    answer = input("Input Your Answer: ")
    
    
    if answer == "1" and fiftyFifty:
    
        fiftyFifty = False
    
        wrongAnswerFifty = random.randint(1, 3)
        correctAnswerFifty = random.randint(1, 2) == 1
    
        if correctAnswerFifty:
    
            print(correctAnswer2)
    
            if wrongAnswerFifty == 1:
                print(var2A)
            elif wrongAnswerFifty == 2:
                print(var2C)
            elif wrongAnswerFifty == 3:
                print(var2D)
    
        elif not(correctAnswerFifty):
    
            if wrongAnswerFifty == 1:
                print(var2A)
            elif wrongAnswerFifty == 2:
                print(var2C)
            elif wrongAnswerFifty == 3:
                print(var2D)

            print(correctAnswer2)
    
        answer = input("Input Your Answer: ")
    
    elif answer == "2" and call:
    
            call = False
    
            enterCall = random.randint (1, 4)
    
            if enterCall == 1:
                print(f"Your friend chose: {var2A}")
            elif enterCall == 2:
                print(f"Your friend chose: {var2B}")
            elif enterCall == 3:
                print(f"Your friend chose: {var2C}")
            elif enterCall == 4:
                print(f"Your friend chose: {var2D}")
    
            answer = input("Input Your Answer: ")
    
    elif answer == "3" and audience:
    
            audience = False
    
            audienceVarD = random.randint(0,30)
            audienceVarC = random.randint(0,30)
            audienceVarA = random.randint(0,30)
            audienceVarB = 100 - (audienceVarD + audienceVarC + audienceVarA)
            
            print(f"{var2A} = {audienceVarA}%")
            print(f"{var2B} = {audienceVarB}%")
            print(f"{var2C} = {audienceVarC}%")
            print(f"{var2D} = {audienceVarD}%")
    
            answer = input("Input Your Answer: ")
    
    
    isCorrect = answer == "B" or answer == "b"
    
    if isCorrect:
        bankomat += 10000


# Question 3


if isCorrect:

    print("\n")

    print("3. " + question3)
    print(var3A)
    print(var3B)
    print(var3C)
    print(var3D)
    
    print("\n")
    
    if fiftyFifty:
        print("Also you can press: ")
        print("1 to 50/50")
    if call:
        print("Also you can press: ")
        print("2 to Call")
    if audience:
        print("Also you can press: ")
        print("3 to Audience")
    
    print("\n")
    
    answer = input("Input Your Answer: ")
    
    
    if answer == "1" and fiftyFifty:
    
        fiftyFifty = False
    
        wrongAnswerFifty = random.randint(1, 3)
        correctAnswerFifty = random.randint(1, 2) == 1
    
        if correctAnswerFifty:
    
            print(correctAnswer3)
    
            if wrongAnswerFifty == 1:
                print(var3B)
            elif wrongAnswerFifty == 2:
                print(var3C)
            elif wrongAnswerFifty == 3:
                print(var3D)
    
        elif not(correctAnswerFifty):
    
            if wrongAnswerFifty == 1:
                print(var3B)
            elif wrongAnswerFifty == 2:
                print(var3C)
            elif wrongAnswerFifty == 3:
                print(var3D)

            print(correctAnswer3)
    
        answer = input("Input Your Answer: ")
    
    elif answer == "2" and call:
    
            call = False
    
            enterCall = random.randint (1, 4)
    
            if enterCall == 1:
                print(f"Your friend chose: {var3A}")
            elif enterCall == 2:               
                print(f"Your friend chose: {var3B}")
            elif enterCall == 3:               
                print(f"Your friend chose: {var3C}")
            elif enterCall == 4:               
                print(f"Your friend chose: {var3D}")
    
            answer = input("Input Your Answer: ")
    
    elif answer == "3" and audience:
    
            audience = False
    
            audienceVarD = random.randint(0,30)
            audienceVarC = random.randint(0,30)
            audienceVarB = random.randint(0,30)
            audienceVarA = 100 - (audienceVarD + audienceVarC + audienceVarB)
            
            print(f"{var3A} = {audienceVarA}%")
            print(f"{var3B} = {audienceVarB}%")
            print(f"{var3C} = {audienceVarC}%")
            print(f"{var3D} = {audienceVarD}%")
    
            answer = input("Input Your Answer: ")
    
    
    isCorrect = answer == "A" or answer == "a"
    
    if isCorrect:
        bankomat += 15000


# Question 4


if isCorrect:

    print("\n")

    print("4. " + question4)
    print(var4A)
    print(var4B)
    print(var4C)
    print(var4D)
    
    print("\n")
    
    if fiftyFifty:
        print("Also you can press: ")
        print("1 to 50/50")
    if call:
        print("Also you can press: ")
        print("2 to Call")
    if audience:
        print("Also you can press: ")
        print("3 to Audience")
    
    print("\n")
    
    answer = input("Input Your Answer: ")
    
    
    if answer == "1" and fiftyFifty:
    
        fiftyFifty = False
    
        wrongAnswerFifty = random.randint(1, 3)
        correctAnswerFifty = random.randint(1, 2) == 1
    
        if correctAnswerFifty:
    
            print(correctAnswer4)
    
            if wrongAnswerFifty == 1:
                print(var4B)
            elif wrongAnswerFifty == 2:
                print(var4C)
            elif wrongAnswerFifty == 3:
                print(var4A)
    
        elif not(correctAnswerFifty):
    
            if wrongAnswerFifty == 1:
                print(var4B)
            elif wrongAnswerFifty == 2:
                print(var4C)
            elif wrongAnswerFifty == 3:
                print(var4A)

            print(correctAnswer4)
    
        answer = input("Input Your Answer: ")
    
    elif answer == "2" and call:
    
            call = False
    
            enterCall = random.randint (1, 4)
    
            if enterCall == 1:
                print(f"Your friend chose: {var3A}")
            elif enterCall == 2:               
                print(f"Your friend chose: {var3B}")
            elif enterCall == 3:               
                print(f"Your friend chose: {var3C}")
            elif enterCall == 4:               
                print(f"Your friend chose: {var3D}")
    
            answer = input("Input Your Answer: ")
    
    elif answer == "3" and audience:
    
            audience = False
    
            audienceVarA = random.randint(0,30)
            audienceVarC = random.randint(0,30)
            audienceVarB = random.randint(0,30)
            audienceVarD = 100 - (audienceVarA + audienceVarC + audienceVarB)
            
            print(f"{var4A} = {audienceVarA}%")
            print(f"{var4B} = {audienceVarB}%")
            print(f"{var4C} = {audienceVarC}%")
            print(f"{var4D} = {audienceVarD}%")
    
            answer = input("Input Your Answer: ")
    
    
    isCorrect = answer == "D" or answer == "d"
    
    if isCorrect:
        bankomat += 20000
        

if isCorrect:
    print(f"You Won And Your Bank {bankomat}")
else:
    print(f"HAHAHA You Lose And Your Bank {bankomat}")