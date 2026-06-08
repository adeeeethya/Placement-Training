#54321
def rec(n):
    if n==0:
        return
    if n%2==0:
        print(n,end=" ")
    rec(n-1)
    if n%2==0 and n>3:
        print(n,end=" ")
n=10
rec(n)