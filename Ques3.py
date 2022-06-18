print("\nWelcome to my Program")
import math
a = int(input("Please enter the length of side 1 : "))
b = int(input("Please enter the length of side 2 : "))
c = int(input("Please enter the length of side 3 : "))
while ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    s = (a + b + c) / 2
    Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("\nArea of the triangle is : ",Area)
    break
while ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("\nThe combination of the sides entered isn't possible !")
    break