import math
N=int(input())
sum1=0
for num in range(19,N):
    sum=0
    for i in str(num):
        sum=sum+math.factorial(int(i))
    if(sum%num==0):
        sum1=sum1+num
print(sum1)
