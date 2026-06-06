#max length of subarray with sum 10
list=[2,1,6,2,1,4,7,8,1,2]
k=10
r,l,s=0,0,0
m=0
while r<len(list):
    s+=list[r]
    while s>k:
        s-=list[l]
        l+=1
    length=r-l+1
    m=max(m,length) #max length found so far m value will be updated with the max value found each time
    r+=1
print(m)