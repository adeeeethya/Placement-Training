l=[1,2,2,2,2,3,3,4,4,4,4,4,4,4,4,5,5]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

ele,max1=0,0
max2=0

for i in d:
    if d[i]>max1:
        max1=d[i]
        ele=i
print(ele)