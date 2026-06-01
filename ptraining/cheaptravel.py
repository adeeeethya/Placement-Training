#466a
n,m,a,b=map(int,input().split())
if a*m<b:
    print(a*n)
else:
    print(n//m*b+min(b,(n-((n//m)*m))*a))

    n-m*n//m