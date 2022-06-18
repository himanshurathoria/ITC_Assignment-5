print("\nWelcome to my Program")
print()
lrange = int(input("Kindly enter the lower limit : "))
uprange = int(input("Kindly enter the upper limit : "))

print("\nPrime numbers between", lrange, "and", uprange, "are : ")

for num in range(lrange, uprange + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)