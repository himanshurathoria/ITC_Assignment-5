print("\nWelcome to my Program")
lrange = int(input("Kindly enter the lower limit of the divisibility range : "))
uprange = int(input("Kindly enter the upper limit of the divisibility range : "))
thenum = int(input("Kindly enter the number that is to be divided : "))
print("\nNumbers divisible in the given range are as follows : ")
for i in range(lrange , uprange + 1):
   if(i%thenum==0):
      print(i)