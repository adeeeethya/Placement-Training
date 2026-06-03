l=[1,2,3,5]
max1,max2=0,0
for i in l:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2 and i!=max1:
        max2=i
print(max2)