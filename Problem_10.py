'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
 
print(sum(list(eratosthenes2(2*pow(10,6)))))

# def number_gen(multiplier):
#     return [(6*multiplier)-1, (6*multiplier)+1]
# i=1
# primes = [2,3,]
# while number_gen(i)[1] <= 2*pow(10,6):
#     primes.extend(number_gen(i))
#     i+=1

# print(f"length is {len(primes)}")

# primes = set(primes)

# i=0
# while i<len(primes):
#     num = list(primes)[i]
#     multiples = {x for x in range(2*num,2*pow(10,6),num)}
#     for x in multiples:
#         if x in primes:
#             primes.remove(x)
#     i+=1

# print(f"new length is {len(primes)}")