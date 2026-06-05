l1=[1,5,6]
l2=[2,3,4,7,8,9]
l3=[]
i,j=0,0
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
while j<len(l2):
    l3.append(l2[j])
    j+=2
while i<len(l1):
    l3.append(l1[i])
    i+=1
print(l3)