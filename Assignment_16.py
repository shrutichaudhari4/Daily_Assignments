# Fibonacci Series : third number is the addition of previous two numbers
# 0,1,1,2,3,5,8,13 
# 1. using Simple iteration
a=0
b=1
c=a+b
list_of_num=[a,b,c]
n=int(input("Enter n: "))
for i in range(c,n+1):
    a=b
    b=c
    c=a+b
    list_of_num.append(c)
print(list_of_num)

# 2. Using recursion
def fibonacci_series(i):
    if i<=1:
        return i
    else:
        return fibonacci_series(i-1)+fibonacci_series(i-2)

num=int(input("Enter num: "))
if num<=0:
    print("Enter positive number")
else:
    print("Fibonacci series",end=" ")
    for i in range(num):
        print(fibonacci_series(i),end=" ")
