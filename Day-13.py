#Text case Conversion
'''
S=input("enter sentence:")
methods=["upper","lower","title","capitalize","swapcase"]
for i in methods:
    if i=="upper":
        print("Upper:",S.upper())
    elif i=="lower":
        print("lower:",S.lower())
    elif i=="title":
        print("title:",S.title())
    elif i=="capitalize":
        print("capitalize:",S.capitalize())
    elif i =="swapcase":
        print("swapcase:",S.swapcase())
print("original:")
if S.isupper():
    print("text is uppercase:",True)
else:
    print("text is not uppercase:",False)
if S.islower():
    print("text is lowercase:",True)
else:
    print("text is not lowercase:",False)
if S.istitle():
    print("text is title:",True)
else:
    print("text is not title:",False)
    print("Mixedletters:")
   
'''
#User name Validator

'''
while True:
    username=input("enter the username:")
    if username == "quit":
        print("ended")
        break   
    if username.isalnum():
        print("it contains only letters and numbers")
    else :
        print("it is contains special charcaters")
    if username.isalpha():
        print("it starts with alphabet")
    else:
        print("it start with numbers or special characters")
    if username.isidentifier():
        print("its valid python identifier")
    else:
        print("its not valid")
    if username.isascii():
        print("Does not contain only letters and number")
    else:
        print("asciii")
'''
#Formatted Student Report

name=['Asha','Rahul','John']
marks=['85','63','35']
for i in range(0,100):
    if marks >= 80:
        print("A")
    elif marks >=60 and <=79:
        print("B")










































