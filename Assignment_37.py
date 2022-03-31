import math
# For understanding
print(math.sqrt(abs(24)))
print(math.sqrt(24))


def find_Roots(a,b,c):
    if a==0:
        print("Invalid")
    d=(b*b)-4*a*c
    square_root=math.sqrt(abs(d))

    if d>0:
        print("Roots are real and different: ")
        print(-b + (square_root)/(2*a))
        print(-b - (square_root)/(2*a))
    elif d==0:
        print("Roots are real and same: ")
        print(-b / (2*a))
    else:
        print("Roots are complex: ")
        print(-b / (2*a),"+i",square_root)
        print(-b / (2*a),"-i",square_root)

find_Roots(1,9,4)
find_Roots(1,4,4)

