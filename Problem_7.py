'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def number_gen(x):
    y = x+1
    while y%6 not in [1,5] :
        y+=1
    return y

counter = 5
primelist = [2,3,5,7,11]
temp=11

while counter!=10001:
    isprime=True
    x = number_gen(temp)
    temp = x
    for i in primelist:
        if i > x**0.5:
            break
        elif x % i == 0:
            isprime = False
            break
    if isprime:
        primelist.append(x)
        counter+=1

print(primelist)
print("number is: ")
print(primelist[-1]) 
