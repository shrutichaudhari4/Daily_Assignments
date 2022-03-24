# In Which Quadrant x and y lies:

x,y=map(int,input("Enter the values of x and y co-ordinate:").split(","))
if x>0 and y>0:
    print(f"{x} and {y} are in First Quadrant")
elif x<0 and y>0:
    print(f"{x} and {y} are in Second Quadrant")
elif x<0 and y<0:
    print(f"{x} and {y} are in Third Quadrant")
elif x>0 and y<0:
    print(f"{x} and {y} are in Fourth Quadrant")
elif x==0 and y==0:
    print(f"{x} and {y} are at Origin Axis")
elif x!=0 and y==0:
    print(f"{x} and {y} are on x-axis")
else:
    print(f"{x} and {y} are on y-axis")


