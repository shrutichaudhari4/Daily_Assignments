# Leap year or not

# 1.if-Elif:
year=int(input("Enter Year you want: "))
if year%4==0 and year%100!=0:
    print("Leap Year")
elif(year%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 2.If-Else
year=int(input("Enter Year you want: "))
if(year%400==0) or (year%100!=0 and year%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")
