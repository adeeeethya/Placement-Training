
#string compression
s="aaaaaaaaaaabbbbbbbbbccccddddddd"
c,k=1,0
res=""
for i in range(1,len(s)):
    if s[k]==s[i]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        c=1 
        k=i
res+=s[-1]+str(c)
print(res)