# Using Iteration
n=int(input("Enter n: "))
sum=0
list_perfect=[]
for i in range(1,n):
    if n%i==0:
        list_perfect.append(i)
# print(list_perfect)
for num in list_perfect:
    sum+=num
# print(sum)
if sum==n:
    print('Its a Perfect Number', n)
    print("And the factors are:")
    print(list_perfect)
else:
    print("Its not a perfect number ", n)

# OR 
# usinh list Comprehension
n=int(input("Enter n: "))
sum=0
list_perfect2=[i  for i in range(1,n) if n%i==0]
for num in list_perfect2:
    sum+=num
Check=[list_perfect2 if sum==n else "Not Perfect"]
print(Check)

