# Two Ways:

# 1.Using Function

def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

print(check(9))
print(check(8))

# 2.Using Ternary Operator

a=int(input("Enter a: "))
check_out="even" if a%2==0 else "odd"
print(check_out)

