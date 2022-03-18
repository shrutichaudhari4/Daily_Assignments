# 12
# 1*12
# 2*6
# 3*4
# 1 + 2 + 3 + 4 + 6=16 > 12 (Abundant Number)
# 21
# 1*21
# 3*7
# 1 + 3 + 7=11 < 21 (Not an Abundant Number)

#Program:

n=int(input("Enter num: "))
factors=[i for i in range(1,n) if n%i==0]
print(factors)
sum=0
for i in factors:
    sum+=i
print(sum)
check=["Abundant" if sum>n else "Not Abundant"]
print(check)
