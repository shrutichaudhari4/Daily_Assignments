# 1. Using count method
num=12323
s=str(num)
print(s.count('3'))

# 2. Using loop
num=1243343
d=3
c=0
for i in str(num):
    if i==str(d):
        c+=1
print("Count of",d,"is",c)

# OR

def count_digit(number,digit):
    count=0
    for i in str(number):
        if i==str(digit):
            count+=1
    print(f"Count of {digit} is {count}")

count_digit(98219,9)
