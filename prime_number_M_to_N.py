def check_is_prime(m, n):
    
    # complete this function
    prime=""
    for i in range(m,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            prime+=str(i)+" "
    return prime
            
m = int(input())
n = int(input())

prime_numbers = check_is_prime(m,n)   # Call the check_is_prime function

print(prime_numbers)

"""
input:
13
29
output:13 17 19 23 29 

"""
