# (x > 0, y > 0)
# *
# **
# ***
# ****
# *****
# ******

print("Hello User")
number = int(input("Input Number: "))
summa = number - number
power = summa + 1
for e in range (0,number):
    e = "*"
    e *= power
    power += 1
    print(e)


# (x > 0, y < 0)
# ******
# *****
# ****
# ***
# **
# *


print("Hello User")
number = int(input("input number: "))
for f in range (0,number):
    f = "*"
    f *= number
    number -= 1
    print(f)




# (x < 0, y > 0)
#      *
#     **
#    ***
#   ****
#  *****
# ******



print("Hello User")
number = int(input("Input Number: "))
for R in range(0,number):
    print(" "*(number-1), "*"*(R+1))
    number -= 1




# (x < 0, y < 0)
# ******
#  *****
#   ****
#    ***
#     **
#      *




print("Hello User")
number = int(input("Input Number: "))
for p in range(0,number):
    print(" " * p,"*" * number)
    number -= 1 



# 2. 
# input: 5
# output:

# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *




print("Hello User")
number = int(input("Input Number: "))
for n in range (0,number + 1):
    print("*"*(n+1),)

for n in range(0,number + 1):
    print("*" * (number + 1))
    number -= 1