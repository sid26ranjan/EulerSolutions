T=int(input())
for i in range(0,T):
    N=int(input())
    sum1=((N*(N+1))//2)**2
    sum2=(N*(N+1)*(2*N+1))//6
    sum=sum1-sum2
    print(sum)
