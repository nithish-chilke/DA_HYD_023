'''
Identity Operators --> checks the identity of an object --> id()

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print (a is c)
print(5 == 5)

a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
'''
#As  we have lists (Mutable collection) both c and a lists will have different
#ids whereas values are same
'''
print(c is a)#output False
print(c == a)#output True
print(a is not c)
'''
#Bitwise operators --> we perform bitwise operations over operands
# & (and) , |(or) , ^(XOR) , shifting operators(<<,>>)
#number will be converted to binary format
"""
print(5&3)#both 3 & 5 converted into binary and bitwise and is performed
print(5|3)#bitwise  OR
print(5^3)#bitwise  XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case
"""
#Leftshift operator << ,right shift operator>>
'''
print(5<<1)#left shift operation by 1
print(7<<3)#left shift operation by 3

print(15 << 2)# converting 15 into binary and perform 2 times shifting
print(15 >> 2)
'''
#Input Formatting --> input().int(input()),float(input())
# you know  -->single input()
# 2 or 3 input --> map()
#group ofinputs--> list(map(int,input().split()))
'''
names = input("enter name :").spilt(',')
print(names)

name 1,name2 = map(str,input("eter the names:").spilt(','))
print(name1,name2)
'''

#tokens -->  Numeric Datatypes --> operators --> flow of program
#control block statements --> they control the flow of program
#conditional statements --> if,else,elif
#repetation statements(loops) --> For , while

#Conditional statement --> IF usage
'''
syntax:
if <condition>:
    statement(S)...
    .....
'''
'''
age = int(input("enter the age:"))
if age >= 18:
    print ("your age is :" , age)
'''
'''
age = int(input("enter the age:"))
if age>=18 and age in [19,21,20]:
    print("your age is:",age)
print(age)
'''

#else keyword usage --> if-else

'''
else:
    statement(s)...

if-else usage as below:

if<condtion>:
    statement(S)...
    ...
else:
    statement(S)...
    ...
'''

#voter eligibility --> by if-else logic
'''
age = int(input("enter the age :"))
if age>=18:
    print("you have voter eligibility and age is :",age)
    print("access Granted")
else:
    age =18-age
    print("you need to wait for more",age,"years.")
'''

#same case y=using nested --> if, else
age = int(input("enter the age :"))
if age >0:
    if age>=18:
        print("you have voter eligibility and age is :",age)
        print("access Granted")
    else:
        age =18-age
        print("you need to wait for more",age,"years.")
else:
    print("ypu have enetered invalid values")






























