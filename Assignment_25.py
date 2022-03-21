# LCM

# 1.Taking Out multiples and search common and return least of it
a=int(input("Enter a:"))
b=int(input("Enter b:"))
mul_a=[(a*i) for i in range(1,max(a,b)+1) ]
mul_b=[(b*j) for j in range(1,max(a,b)+1)]
# print(mul_a)
# print(mul_b)
common=[each for each in mul_a if each in mul_b]
print(min(common))
        
    
# 2. Using Formula
a=int(input("Enter a:"))
b=int(input("Enter b:"))
hcf=1
for i in range(1,max(a,b)):
    if a%i == b%i ==0:
        hcf=i

lcm=(a*b)//hcf
print(lcm)
    # print(i)
