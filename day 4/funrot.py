l=[1,2,3,4,5,6,7]
k=int(input("enter the number of rotations:"))
n=len(l)
k=k%n
def rotate(i,j):
    while i<=j:
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1
rotate(0,n-1)
rotate(0,k-1)
rotate(k,n-1)
print(l)
    