n,e=map(int, input().split())
result=1
while e>0:
    if e&1:
        result*=n
    n*=n
    e>>=1
print(result)
