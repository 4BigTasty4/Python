import random

answer = True

fiftyFifty = True
audience = True
call = True

bankomat = 0

AllQuestion = ["0 - 1 = ?","2 + 2 = ?","0 * 1 = ?"]

QuestionVariants1 = ["A) !1","B) 1","C) -1","D) 10"]
QuestionVariants2 = ["A) 4","B) 5","C) 1","D) -4"]
QuestionVariants3 = ["A) !1","B) 1","C) 10","D) 15"]

AllRightVariant = ["C) -1","B) 5","A) !1"]

correctAnswerBig = ["A","B","C"]
correctAnswerSmall = ["a","b","c"]

def FiftyFiftyHelper():

    global fiftyFifty
    global answer

    fiftyFifty = False

    wrongAnswerFifty = random.randint(1, 3)
    correctAnswerFifty = random.randint(1, 2) == 1
    
    if correctAnswerFifty:
    
        print(AllRightVariant[0])
    
        if wrongAnswerFifty == 1:
            print(QuestionVariants1[0])
        elif wrongAnswerFifty == 2:
            print(QuestionVariants1[1])
        elif wrongAnswerFifty == 3:
            print(QuestionVariants1[3])
    
    elif not(correctAnswerFifty):
    
        if wrongAnswerFifty == 1:
            print(QuestionVariants1[0])
        elif wrongAnswerFifty == 2:
            print(QuestionVariants1[1])
        elif wrongAnswerFifty == 3:
            print(QuestionVariants1[3])

        print(AllRightVariant[0])

    answer = input("Input Your Answer: ")

def FiftyFiftyHelper1():

    global fiftyFifty
    global answer

    fiftyFifty = False

    wrongAnswerFifty = random.randint(1, 3)
    correctAnswerFifty = random.randint(1, 2) == 1
    
    if correctAnswerFifty:
    
        print(AllRightVariant[1])
    
        if wrongAnswerFifty == 1:
            print(QuestionVariants2[0])
        elif wrongAnswerFifty == 2:
            print(QuestionVariants2[2])
        elif wrongAnswerFifty == 3:
            print(QuestionVariants2[3])
    
    elif not(correctAnswerFifty):
    
        if wrongAnswerFifty == 1:
            print(QuestionVariants2[0])
        elif wrongAnswerFifty == 2:
            print(QuestionVariants2[2])
        elif wrongAnswerFifty == 3:
            print(QuestionVariants2[3])

        print(AllRightVariant[1])

    answer = input("Input Your Answer: ")

def FiftyFiftyHelper2():

    global fiftyFifty
    global answer

    fiftyFifty = False

    wrongAnswerFifty = random.randint(1, 3)
    correctAnswerFifty = random.randint(1, 2) == 1
    
    if correctAnswerFifty:
    
        print(AllRightVariant[2])
    
        if wrongAnswerFifty == 1:
            print(QuestionVariants3[1])
        elif wrongAnswerFifty == 2:
            print(QuestionVariants3[2])
        elif wrongAnswerFifty == 3:
            print(QuestionVariants3[3])
    
    elif not(correctAnswerFifty):
    
        if wrongAnswerFifty == 1:
            print(QuestionVariants3[1])
        elif wrongAnswerFifty == 2:
            print(QuestionVariants3[2])
        elif wrongAnswerFifty == 3:
            print(QuestionVariants3[3])

        print(AllRightVariant[2])

    answer = input("Input Your Answer: ")

def CallHelper():

    global call
    global answer

    call = False

    enterCall1 = random.randint (1, 4)

    if enterCall1 == 1:
        print(f"Your friend chose: {QuestionVariants1[0]}")
    elif enterCall1 == 2:
        print(f"Your friend chose: {QuestionVariants1[1]}")
    elif enterCall1 == 3:
        print(f"Your friend chose: {QuestionVariants1[2]}")
    elif enterCall1 == 4:
        print(f"Your friend chose: {QuestionVariants1[3]}")

    answer = input("Input Your Answer: ")

def CallHelper1():

    global call
    global answer

    call = False

    enterCall1 = random.randint (1, 4)

    if enterCall1 == 1:
        print(f"Your friend chose: {QuestionVariants2[0]}")
    elif enterCall1 == 2:                           
        print(f"Your friend chose: {QuestionVariants2[1]}")
    elif enterCall1 == 3:                           
        print(f"Your friend chose: {QuestionVariants2[2]}")
    elif enterCall1 == 4:                           
        print(f"Your friend chose: {QuestionVariants2[3]}")

    answer = input("Input Your Answer: ")

def CallHelper2():

    global call
    global answer
    
    call = False
    
    enterCall1 = random.randint (1, 4)
    
    if enterCall1 == 1:
        print(f"Your friend chose: {QuestionVariants3[0]}")
    elif enterCall1 == 2:                           
        print(f"Your friend chose: {QuestionVariants3[1]}")
    elif enterCall1 == 3:                           
        print(f"Your friend chose: {QuestionVariants3[2]}")
    elif enterCall1 == 4:                            
        print(f"Your friend chose: {QuestionVariants3[3]}")
    
    answer = input("Input Your Answer: ")

def AudienceHelper():

    global audience
    global answer
    
    audience = False

    audienceVarD = random.randint(0,30)
    audienceVarB = random.randint(0,30)
    audienceVarA = random.randint(0,30)
    audienceVarC = 100 - (audienceVarD + audienceVarB + audienceVarA)
    
    print(f"{QuestionVariants1[0]} = {audienceVarA}%")
    print(f"{QuestionVariants1[1]} = {audienceVarB}%")
    print(f"{QuestionVariants1[2]} = {audienceVarC}%")
    print(f"{QuestionVariants1[3]} = {audienceVarD}%")

    answer = input("Input Your Answer: ")

def AudienceHelper1():

    global audience
    global answer
    
    audience = False

    audienceVarD = random.randint(0,30)
    audienceVarC = random.randint(0,30)
    audienceVarA = random.randint(0,30)
    audienceVarB = 100 - (audienceVarD + audienceVarC + audienceVarA)
    
    print(f"{QuestionVariants2[0]} = {audienceVarA}%")
    print(f"{QuestionVariants2[1]} = {audienceVarB}%")
    print(f"{QuestionVariants2[2]} = {audienceVarC}%")
    print(f"{QuestionVariants2[3]} = {audienceVarD}%")

    answer = input("Input Your Answer: ")

def AudienceHelper2():

    global audience
    global answer
    
    audience = False

    audienceVarD = random.randint(0,30)
    audienceVarB = random.randint(0,30)
    audienceVarC = random.randint(0,30)
    audienceVarA = 100 - (audienceVarD + audienceVarB + audienceVarC)
    
    print(f"{QuestionVariants3[0]} = {audienceVarA}%")
    print(f"{QuestionVariants3[1]} = {audienceVarB}%")
    print(f"{QuestionVariants3[2]} = {audienceVarC}%")
    print(f"{QuestionVariants3[3]} = {audienceVarD}%")

    answer = input("Input Your Answer: ")

def Familiarization():

    print("Hello User Welocome To Milionaire Game! \n")

    name = input("Input Your Name: ")
    
    print("\n")
    
    print(f"{name} This is Victory Table:")
    
    print("\n")
    
    print("3 - rd. question - 15000$")
    print("2 - nd. question - 10000$")
    print("1 - st. question - 5000$")

    print("\n")

Familiarization()

def Myquestion1():
    print("1. " + AllQuestion[0])
    for i in QuestionVariants1:
        print(i)
    if fiftyFifty:
        print("Also you can press: ")
        print("1 to 50/50")
    if call:
        print("Also you can press: ")
        print("2 to Call")
    if audience:
        print("Also you can press: ")
        print("3 to Audience")

Myquestion1()

if answer:
    answer = input("Input Your Answer: ")
    if answer == "1" and fiftyFifty:
        FiftyFiftyHelper()
    elif answer == "2" and call:
        CallHelper()
    elif answer == "3" and audience:
        AudienceHelper()

def Myquestion2():
    print("2. " + AllQuestion[1])
    for i in QuestionVariants2:
        print(i)
    if fiftyFifty:
        print("Also you can press: ")
        print("1 to 50/50")
    if call:
        print("Also you can press: ")
        print("2 to Call")
    if audience:
        print("Also you can press: ")
        print("3 to Audience")

if answer == correctAnswerBig[2] or answer == correctAnswerSmall[2]:
    Myquestion2()
    bankomat += 5000
else:
    answer = False
    print(f"You Lose and Your Bank: {bankomat}$")

if answer:
    answer = input("Input Your Answer: ")
    if answer == "1" and fiftyFifty:
        FiftyFiftyHelper1()
    elif answer == "2" and call:
        CallHelper1()
    elif answer == "3" and audience:
        AudienceHelper1()

def Myquestion3():
    print("3. " + AllQuestion[2])
    for i in QuestionVariants3:
        print(i)
    if fiftyFifty:
        print("Also you can press: ")
        print("1 to 50/50")
    if call:
        print("Also you can press: ")
        print("2 to Call")
    if audience:
        print("Also you can press: ")
        print("3 to Audience")

if answer:
    if answer == correctAnswerBig[1] or answer == correctAnswerSmall[1]:
        Myquestion3()
        bankomat += 10000
    else:
        answer = False
        print(f"You Lose and Your Bank: {bankomat}$")

if answer:
    answer = input("Input Your Answer: ")
    if answer == "1" and fiftyFifty:
        FiftyFiftyHelper2()
    elif answer == "2" and call:
        CallHelper2()
    elif answer == "3" and audience:
        AudienceHelper2()
    if answer == correctAnswerBig[0] or answer == correctAnswerSmall[0]:
        bankomat += 15000
        print(f"You Won And Your Bank: {bankomat}$")
    else:
        print(f"You Lose and Your Bank: {bankomat}$")
