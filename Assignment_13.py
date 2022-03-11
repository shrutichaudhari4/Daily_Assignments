# Palindrome : The number or name you entered is same when you read back to front or vice versa
# Eg: 121=True,nitin=True,1234=false
#  Through slicing and list comprehension
num=int(input("ENter num: "))
num=str(num)
rev_num=num[::-1]
check=[True if num==rev_num else False]
print(check,"Its a palindrome",rev_num)

# OR
name=input("Enter name: ")
check_palindrome=["Palindrome" if name==str(name[::-1]) else "Not a Palindrome"]
print(check_palindrome)


# Using For loop
n=input("Enter num: ")
sum=""
for i in n:
    sum=i+sum  #-->1 Iteration.3+""='3' , 
                # -->2 Iteration.4+'3'='43',
                # -->3 Iteration.5+'43'=543
# print(sum)
if(n==sum):
    print("Palindrome")
else:
    print("Not a palindrome")
