T=int(input())
for j in range(0,T):
    N=int(input())
    sum=1
    for i in range(1,N+1):
        sum=sum*i
    temp = sum
    sum1=0
    while temp > 0:
       digit = temp % 10
       sum1 += digit
       temp //= 10
    print(sum1)

