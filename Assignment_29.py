# Prime Numbers from 1 to 100
l=[]
for i in range(2,100+1):
    # print(i)
    f=0
    for j in range(2,i+1):
        # print(f"{i} and {j}")
        if(i!=j and i%j==0):
            f=1
            break
    if(f==0):
        l.append(i)
print(l,sep=',')

    

    
