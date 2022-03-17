# Prime Factors of a Number:

def prime(num):
        factors=[i for i in range(2,num) if num%i==0]
        if len(factors)==0:
            return True
        else:
            return False
    
# print(prime(10))
# print(prime(9))
# print(prime(5))
# print(prime(3))

n=int(input("Enter n: "))
factors=[i for i in range(2,n) if n%i==0]
prime_factors=[i for i in factors if prime(i)]
for j in prime_factors:
    print(j,end=' ')
