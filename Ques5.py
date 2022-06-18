print("\nWelcome to my Program")
asciichr = 65
num = int(input("Kindly enter the number of rows : "))
for i in range(0,num):
    for j in range(0,i+1):
        if asciichr > 90:
            asciichr = 65
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()