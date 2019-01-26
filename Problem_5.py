l = [x for x in range(2,21)]
values = l[:]
used=0
ans=1
index=0

print("l is  : "+str(l))

while len(l)!=0:
    print("ans is :"+str(ans))
    used=0
    if index>18:
        index = 0
    for i in l:
        if i == 1:
            l.remove(i)
    for i in range(0,len(l)):
        #print("{0} = index , {1}=i ".format(index,i))
        if l[i]%values[index]==0:
            used = 1
            l[i]=int(l[i]/values[index])
    if used:
        ans=ans*values[index]
    index+=1
    print("l is  : "+str(l))

print(ans)
