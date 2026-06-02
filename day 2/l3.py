#segregate the given list as even elements firs tin descending order and then odd elements next in ascending order

l=[1,2,3,4,5,6,7,8,9]
l.sort()
res=[]

for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)
