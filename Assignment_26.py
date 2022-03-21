# GCD:
a=int(input("Enter a:"))
b=int(input("Enter b:"))
gcd=1
for i in range(1,min(a,b)):
    if a%i == b%i ==0:
        gcd=i
print("GCD is ", gcd)

#GCD
a=int(input("Enter a: "))
b=int(input("Enter b: "))
factors_a=[i for i in range(1,a+1) if a%i==0]
factors_b=[i for i in range(1,b+1) if b%i==0]
# print(factors_a)
# print(factors_b)
common=[i for i in factors_a if i in factors_b]
# print(common)
print("HCF is",max(common))
