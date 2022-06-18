print("\nWelcome to my Program")
postivenum=[]
negativenum=[]
oddnum=[]
evennum=[]
occurrence={}
list=[]
for i in range(10):
    num=int(input("Kindly enter the number : "))
    list.append(num)
    if num>=0:
        postivenum.append(num)
    elif num<0 :
        negativenum.append(num)
    if num%2==0 :
        evennum.append(num)
    elif num%2!=0 :
        oddnum.append(num)
    if num not in occurrence :
            occurrence[num]=1
    elif num in occurrence :
        occurrence[num]+=1
print("Positive Numbers : ",postivenum)
print("Negative Numbers : ",negativenum)
print("Even Numbers : ",evennum)
print("Odd Numbers : ",oddnum)
print("Occurrence of each number in the List : ",occurrence)