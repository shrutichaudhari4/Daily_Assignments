# Octal to Decimal
# Octal Number: 246    (Here,^ = raise to or exponential or power)
# 6*8^0 = 6*1 = 6
# 4*8^1 = 4*8 = 32
# 2*8^2 = 2*64 = 128
# 128 + 32 + 6 = 166
num=(input("Enter n: "))
n=num
a=8
sum=0
for i in num:
    l=len(str(num))
    l1=int(l-1)
    oct=a**l1
    sum+=int(i)*oct
    num=int(num)//10
print(f"The Decimal number of {n} is {sum}")
