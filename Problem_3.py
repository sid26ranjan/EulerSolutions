'''
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

answer=0

def is_prime(x):
    if x%6 not in [1,5]: #a prime number must always be of the form (6k+1) or (6k-1)
        return False
    i=2
    while i<=int(x**(1/2)+1):
        if x%i==0:
            return False
        i+=1
    return True

def factors_of(n):
    n_2 = n**(1/2)
    i=2
    factors = []
    while i<=n_2:
        if n%i==0:
            factors.append([i,n/i])
        i+=1
    return factors

factors = factors_of(600851475143)

for (i,j) in factors:
    '''
    j is initially the largest factor
    as we iterate through factors list the value of j decreases
    the first j to be prime is the answer
    '''
    if is_prime(j):
        answer = j
        break
    elif is_prime(i):
        answer = i
    #the last occurance of i which is prime is the largest prime factor (in case no j is prime)
print(answer)