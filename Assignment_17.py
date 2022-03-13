#1. Using for loop

num=int(input("enter num: "))
fact=1
for i in range(fact,num+1):
    fact=fact*i 
print("The factorial of", num ," is", fact)

# 2.
def factorial(n):
    f=1
    i=1
    if n<0:
        print("Enetr positive number")
    else:
        while(i<=n):
            f*=i 
            i=i+1
    return f
print(factorial(5))
