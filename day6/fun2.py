#12345
def rec(n):
    if n==0:
        return 200
    else:
        rec(n-1)
        print(n,end=" ")
n=int(input("enter the number:"))
rec(n)