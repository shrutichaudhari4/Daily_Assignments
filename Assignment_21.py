# Harshad Number
# 153/1+5+3 = 17
# 408/4+0+8 = 34
n=int(input("Enter n: "))
sum=0
for i in str(n):
    sum+=int(i)
if(n%sum==0):
    print(n//sum)
else:
    print("Not Divisible")

# OR

num=int(input("Enter num: "))
sum=0
for i in str(n):
    sum+=int(i)
ans=[n//sum if n%sum==0 else "Not Divisible"]
print(ans)



    
