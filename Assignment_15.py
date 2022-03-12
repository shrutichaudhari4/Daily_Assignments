# Armstrong Number within a range

def Armstrong(num):
     # num=input("ENter num: ")
     check_num=num
     length=len(str(num))
     sum=0
     for i in str(num):
         sum+=pow(int(i),length)
     # print(sum)
     if(check_num==sum):
         print(num," Armstrong Number")
     else:
         print(num," Not an Armstrong Number")
         

num=int(input("ENter num: "))   #num to start from-->eg:150
second=int(input("Enter second:"))   #num to end with-->eg:160
for i in range(num,second+1):
    Armstrong(i)
