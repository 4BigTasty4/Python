winers = ["Elnur, Zabil, Elvin"]
lose = ["Dan, Steve"]


print("Hello User")
global name, surname, bank, answer
def LoginGame(name, surname):
 

 print(f"\n{name} {surname} Welcome to Millionaire Game! \n")


 print("Victory table")
 print("5-rd. question - 5000$")
 print("4-rd. question - 4000$")
 print("3-rd. question - 3000$")
 print("2-nd. question - 2000$")
 print("1-st. question - 1000$ \n")

name = input("Input Your Name: ")
surname = input("Input Your Surname: ")


LoginGame(name, surname)


bank = 0       
print("\nQuestion: 1\nHow Much Will 2 + 2: ")
print("A)5\nB)4\nC)2\nD)8")
answer = input("Input Your Answer: ")  
if answer == "B" or answer == "b":
    print("Succses\n")
    bank += 1000
else:
    print(f"\nYou Lose and Your Bank: {bank}$")
    lose.append(name)
    print(f"\nYou Are On The Losing List: {lose}")
if answer == "B" or answer == "b":
    print("Question: 2\nHow Much Will 5 * 4: ")
    print("A)35\nB)13\nC)20\nD)27")
    answer = input("Input Your Answer: ")
    if answer == "C" or answer == "c":
     print("Succses\n")
     bank += 2000
    else:
        print(f"You Lose and Your Bank: {bank}$")
        lose.append(name)
        print(f"\nYou Are On The Losing List: {lose}")
    if answer == "C" or answer == "c":
     print("Question: 3\nHow Much Will 145 - 150: ")
     print("A)-5\nB)125\nC)-55\nD)295")
     answer = input("Input Your Answer: ")
     if answer == "A" or answer == "a":
       print("Succses\n")
       bank += 3000
     else:
         print(f"You Lose and Your Bank: {bank}$")
         lose.append(name)
         print(f"\nYou Are On The Losing List: {lose}")
     if answer == "A" or answer == "a":
       print("Question: 4\nHow Much Will 50 / 25: ")
       print("A)5\nB)2\nC)1\nD)0")
       answer = input("Input Your Answer: ")
       if answer == "B" or answer == "b":
        print("Succses\n")
        bank += 4000
       else:
         print(f"You Lose and Your Bank {bank}$")
         lose.append(name)
         print(f"/nYou Are On The Losing List: {lose}")
       if answer == "B" or answer == "b":
         print("Question: 5\nHow Much Will (10 + 5)*5: ")
         print("A)75\nB)5\nC)25\nD)15")
         answer = input("Input Your Answer: ") 
         if answer == "A" or answer == "a":
           print("Succses\n")
           print(f"Congratulations You Won And Your Winnings Are: {bank}$ ")
           winers.append(name)
           print(f"\nYou Are On The List Of Winners: {winers}")
           bank += 5000
         else:
          print(f"You Lose and Your Bank: {bank}$")
          lose.append(name)
          print(f"\nYou Are On The Losing List: {lose}")

