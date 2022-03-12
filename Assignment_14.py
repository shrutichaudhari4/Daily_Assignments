# Armstrong Number:

n=int(input("Enter num: "))
temp=n
sum=0
while(n!=0):
    digit=n%10
    sum+=digit**3
    n=n//10

if(temp==sum):
    print("Its an Armstrong Number")
else:
    print("Its not an Armstrong number")


num=input("ENter num: ")
check_num=num
length=len(num)
sum=0
for i in num:
    sum+=pow(int(i),length)
# print(sum)
if(check_num==sum):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

