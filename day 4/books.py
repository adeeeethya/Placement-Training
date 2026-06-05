books=[2,1,3,1,3,4,2,1,3,4,6,7,8,1,2]
k=3
n=len(books)
s=sum(books[:k])
m=s
for i in range(1,n-k+1):
    s=s-books[i-1]+books[i+k-1]
    m=max(m,s)
print(m)