# Binary To Decimal:

# 101101 : (base=32,16,8,4,2,1)
# 1*32 + 0*16 + 1*8 + 1*4 + 0*2 + 1*1 = 183
num=int(input("Enter binary number: "))
bin=num
base=1
binary_num=0
while(num>0):
    rem=num%10
    binary_num=binary_num+rem*base
    num=num//10
    base=base*2
print(binary_num)

num=int(input("Enter num: "))
num_s=str(num)
sum=1
rem=0
while(num>0):
    # rem=num%10
    sum+=(2**len(num_s))*rem
    num=num//10
    rem=num%10
    num_s=str(num)
print(sum)
