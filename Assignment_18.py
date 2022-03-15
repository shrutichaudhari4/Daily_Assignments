# Calculate the power to a number:

# 1.using pow function
num,power=2,3
print(pow(num,power))

# 2.Using Iteration
num=int(input("Enter num: "))
power=int(input("Enter power you want:"))
output=1
for i in range(power):
    output*=num
    # print(output)
print("Power of ", num, "is", output)

# 3. Using Python Exponential (**) Operator
num,power=2,4
print(2**4)
