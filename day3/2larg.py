l=[1,2,3,4,5,6]
max1=0
for i in l:
    if i>max1:
        max1=i
max2=0
for i in l:
    if i>max2 and i!=max1: #finding max again such that it is not max1
        max2=i
print(max2)
