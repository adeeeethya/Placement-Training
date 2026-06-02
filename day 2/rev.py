n=int(input("no:"))
rev=0
while n:
    d=n%10 #get last digit
    rev=rev*10+d #add digit from beginning
    n=n//10 #remove the last digit from number
print(rev)