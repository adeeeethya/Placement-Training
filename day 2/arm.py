n=int(input("enter numbr:"))
temp=n
count=0
arm=0
st=str(n)
l=len(st)
k=int(l)
while n:
    d=n%10
    arm=arm+d**k
    n=n//10
if temp==arm:
    print("armstrong number")
else:
    print("not armstrong")

