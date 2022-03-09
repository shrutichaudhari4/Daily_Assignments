# Greatest among three numbers

# Using If-Elif:
a,b,c=input("Enter three numbers: ").split(",")
if a>b and a>c:
    print("a is greatest" , a)
elif(b>c):
    print("b is greatest", b)
else:
    print("c is greatest", c)

# Nested If-Else:
a,b,c=input("Enter three numbers: ").split(",")
if a>b:
    if a>c:
        print('a is greatest', a)
elif(b>a):
    if b>c:
        print('b is greatest', b)
    else:
        print("c is greatest", c)

# Using Ternary Operator
a,b,c=input("Enter three numbers: ").split(",")
Greater=a if a>b else b
Greatest=c if c>Greater else Greater
print(Greatest)
    

# User Input : Should be written aas:
# 1,3,5 #Numbers can be user-defined
