'''
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

i = 1
sum = 0
n = int(input("Enter n:"))
while i<n:
    if i%3==0 or i%5==0:
        print(i)
        sum = sum + i
    i+=1

print("answer is : %s"%sum)

'''
Better Approach:
Use (AP Series Sum of :) 3 + 5 - 15

'''
