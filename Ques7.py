print("\nWelcome to my Program")
print("\nBetween 1 and 500 the following numbers are multiple of 7 : ")
for i in range(1,501) :
    if i%7 == 0 :
        print(i)
print("\nBetween 1 and 500 the following numbers are divisible by 11 : ")
for i in range(1,501) :
    if i%11 == 0 :
        print(i)
print("\nBetween 1 and 500 the following numbers are both multiple of 7 and divisible by 11 : ")
for i in range(1,501) :
    if i%7 == 0 and i%11 == 0 :
        print(i)