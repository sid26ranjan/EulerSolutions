N=int(input())
sum1=0
for num in range(0,999999):
    sum=0
    for i in str(num):
        sum=sum+(int(i)**N)
    if(sum==num):
        sum1=sum1+num
print(sum1-1)
