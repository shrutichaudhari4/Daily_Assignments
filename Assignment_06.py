#Greatest Among Two Numbers

# 1.Using If-Else
a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a>b:
    print(a)
print(b)

# 2.Using Function
def greatest(a,b):
    if a>b:
        return a
    return b
print(greatest(9,6))

# 3.Using Ternary Operator
a=20
b=30
Greatest_num= a if a>b else b
print(Greatest_num)

# 4.Using Inbuilt-Function max()
a,b=10,80
print(max(a,b))
