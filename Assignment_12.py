# Reverse of a Number

# Using Slicing
n=input("Enter num: ")
print(n[::-1])

# using while loop
n=int(input("Enter Number: "))
sum=""
while(n!=0):
    digit=int(n)%10
    sum+=str(digit)
    n=n//10
print(int(sum))

# Using For loop
n=input("Enter num: ")
sum=""
for i in n:
    sum=i+sum  #-->1 Iteration.3+""='3' , 
                # -->2 Iteration.4+'3'='43',
                # -->3 Iteration.5+'43'=543
print(sum)


# Using Simple Iteration
num=1234
temp=num
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)
