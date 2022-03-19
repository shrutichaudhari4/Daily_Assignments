# !.Using Factors
a=int(input("Enter a: "))
b=int(input("Enter b: "))
factors_a=[i for i in range(1,a+1) if a%i==0]
factors_b=[i for i in range(1,b+1) if b%i==0]
print(factors_a)
print(factors_b)
common=[i for i in factors_a if i in factors_b]
# print(common)
print("HCF is",max(common))


# OR
#2. Using If-Else
num1 = 36
num2 = 60
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("Hcf of", a, "and", b, "is", num1)


#OR
# 3.Using for
num1=9
num2=18
hcf=1
for i in range(1, min(num1, num2)):

    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("Hcf of", num1, "and", num2, "is", hcf)
