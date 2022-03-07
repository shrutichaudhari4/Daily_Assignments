# Sum Till n numbers 

# 1.Using For Loop
a=int(input("Enter a: "))
b=int(input("Enter b: "))
for i in range(a,b):
    a=a+(i+1)
print(a)

# OR

a=int(input("Enter a: "))
b=int(input("Enter b: "))
sum=0
for i in range(a,b+1):
    sum+=i
print(sum)


# Using Recursion
def recursum(sum,n1,n2):
  if n1 > n2:
    return sum
  return n1 + recursum(sum,n1+1,n2)

print(recursum(0,3,6))
