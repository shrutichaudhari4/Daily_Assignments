# Three ways
#To Check Number is positive or negative

# 1.Using if else
n=int(input("Enter num: "))
if(n==0):
    print("Number is zero")
elif(n>0):
    print("Its a positive number")
else:
    print("Its a negative number")


# 2.Using TErnary Operator
a=int(input("Enter num: "))
check="Positive" if a>0 else "Negative"
print(check)

# 3.Using Nested If-else
x=int(input("Enter num: "))
if x>=0:
    if x==0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
