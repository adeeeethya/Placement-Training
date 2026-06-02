n=int(input("enter numbr:"))
temp=n
count=0
arm=0
st=str(n)
l=len(st)
k=int(l)

i=1
while n:
    d=n%10
    arm=arm+d**k
    k=k-1
    n=n//10
print(arm)


