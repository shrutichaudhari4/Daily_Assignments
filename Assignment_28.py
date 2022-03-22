#Decimal to binary
# 56 = 56%2 = Remainder = 0
# 28%2 = Remainder = 0
# 14%2 = Remainder = 0
# 7%2 = Remainder = 1
# 3%2 = Remainder = 1
# Reaminder =1 
# Reading Remainder reverese = 111000

num=int(input("Enter num: "))
bin=[]
while(num!=0):
    bin.append(num%2)
    num=num//2
bin.reverse()
for j in bin:
    print(j,end="")
    

