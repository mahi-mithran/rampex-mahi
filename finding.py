n=int(input())
m=list(map(int,input().split()))
t=int(input())
for i in range(n):
    for j in range(1+i,n):
        if m[i]+m[j]==t:
            print(i,j)
    