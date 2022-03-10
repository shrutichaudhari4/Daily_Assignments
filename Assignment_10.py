#Prime numbers within a range

a=int(input("Enter number: "))
primes=[]
for i in range(2,a+1):
    prime=False
    if(a<0):
        continue
    if(a==2):
        primes.append(2)
        continue
    for num in range(2,i):
        if(i%num==0):
            prime=True
            break
    if prime==False:
        primes.append(i)
print(primes)
