password = input("Enter Password:")
upper=False
lower=False
digit=False
sepcial=False
space=False
for ch in password:
    if ch.isupper():
        upper = True
    elif ch==" ":
        space=True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special and space!=True:
    print("Valid Password")
else:
    print("Invalid Password")