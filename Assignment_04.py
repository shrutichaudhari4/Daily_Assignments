#Sum Of n Numbers:

# 1.Using For Loop
n=int(input("Enter num: "))
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)




# 2.Using Function / Recursion
def Get_Sum(num):
    x=1
    sum_Of_n_num=0
    while(x<=num):
        sum_Of_n_num=sum_Of_n_num+x
        x=x+1
    return sum_Of_n_num
print(Get_Sum(5))

# OR

def Get_Sum2(n):
    if n==1:
        return 1
    return n+Get_Sum2(n-1)

print(Get_Sum2(5))




