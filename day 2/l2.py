l = [1, 1, 2, 2, 3, 3,4,4,4]
l1 = []

for i in l:
    if i not in l1 and l.count(i)%2!=0:
        l1.append(i)

print(l1)