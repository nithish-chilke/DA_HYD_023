'''
cart=list(map(int,input("enter the price:").split(',')))
total=0
for i in  cart:
    total += i
print(total)   

'''
'''
password=input("enter the password:")
print(password)
upper=0
lower=0
digit=0
special=0
for i in password:
    if 'A' <= i <= 'Z' :
        upper += 1
    elif 'a' <= i  <= 'z' :
        lower +=1
    elif '0' <= i <= '9':
        digit +=1
    else:
        special += 1
print("upper:",upper)
print("lower:",lower)
print("digit:",digit)
print("special:",special)
'''

mail=input().split()
for email in mail:
    print(email.split('@'))
    

