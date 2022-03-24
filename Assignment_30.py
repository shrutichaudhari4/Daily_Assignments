# Decimal to Octal:

dec_num=int(input("Enter : "))
oct_num=[]
while(dec_num!=0):
    rem=dec_num%8
    dec_num=dec_num//8
    oct_num.append(rem)
num=oct_num[::-1]
for i in num:
    print(i,end='')


