i=999
j=999
ans = 0
def is_pal(x):
    return str(x) == str(x)[::-1]

for i in range(100,1000,-1):
    for j in range(100,1000,-1):
        if is_palin(i*j):
            ans = max(i*j,ans)
            
print(ans)
