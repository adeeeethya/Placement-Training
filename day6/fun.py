#54321
def rec(n):
    if n==0:
        return
    else:
        print(n,end=" ")
        rec(n-1)
n=int(input("enter the number:"))
rec(n)