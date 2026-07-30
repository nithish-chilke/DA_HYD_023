
#Numeric datatype --> int,float,complex along with boolean

#Input formatting -->Accepting input from the user --> input()

#Accepting integer input from user
#by default input() accepts any input -->str
#int(input()) --> will accpets any integers
'''
age = int(input ('Enter the age:'))
print(age)
print(type(age))
'''
#float (input()) --> accepts integers ,float values
'''
age = float(input ('Enter the age:'))
print(age)
print(type(age))
'''
#Accepting string input from user
'''
age = input ('Enter the age:')
print(age)
print(type(age))
'''

#Accept group of values
'''
marks = int(input("enter the marks:")).split()
print (marks)
'''
'''
a=input().split()#by default split as space
print(a)
'''
#space seperated values
'''
a=input().split() #now enter spaces 
print(a)
'''
#comma seperated values
'''
a=input("Enter the value:").split(',')  
print(a)
'''
#list of integers
'''
marks = list(map(int,input("enter the marks:").split(',')))
print (marks)
'''
#now we wanted to accept 2 values from user
'''
age,salary = map(int,input("enter the values:").split(','))
print(age)
print(salary)
'''

#single input --> int(input())
#two inputs -->a,b = map(int,input().split(','))
#any number result as list --> a=list(map(int,input().split(',')))

#float of integers
'''
age,salary = map(float,input("enter the values:").split(','))
print(age)
print(salary)
'''
'''
marks = list(map(float,input("enter the marks:").split(',')))
print (marks)
'''

#Accepting input from user --> int,float -> input formatting

#Operators --> operators perform operations between values (operands)
#7 types --> Arithmetic,assignment,comparision (Relationship)
#membership,identity,logical,bitwise

#arithemetic operators --. Arithmetic operations
# +,-,*,/
'''
print(5+3)
print(5-3)
print(5*3)
print(5/3)

#floor division (integer division ) --> returns quotient
print(5//5)
#modules --> divisible rules -> returns remainder
print(5%3)
#power (exponential)
print(5**3)
'''
#Task --> Accept integer input as length,breadth --> find area of rectangle
'''
length = int(input("enter the value:"))
breadth = int(input("enter the value:"))
area = length * breadth
print(area)
'''
'''
l,b= map(int,input("enter the value:").split(','))
area = l* b
print(area)
'''
#Assignment operators --> assign the values
# = , += -+
'''
a=45
print(a)
#update a
a = a+5
print(a)
b=35
b += a
print(b)
b -= 5
print(b)
c=2
c *= b
print(c)
d = 5
d -= c #d= d-c
print(d)
'''
#comparision operators --> we compare the values -->boolean
#   ==(equal to) , !=(not equal to) , <(less than) , >(greater than),
#<=(less than or equal to) , >=( greater than or equal to ),
'''
age = 25
print(age == 25)
print(age != 25)
print(age < 25)
print(age > 25)
print(age <= 25)
print(age >= 35)
print(-5 > -25)
'''
#membership operators --> in,not in -->boolean
#it checks for the existance of an object in an collection
'''
marks = [56,57,47,35]
print(35 in marks)

print(25 not in marks)
print('code' in 'codegnan')
'''

#logical operators --> Logical decision making --> and,or,not
#and --> all conditions to be satisfied
#or --> any one condition to be satisified
'''
a= (25 in [24,25,45]) and 45 > 56
print(a)
b = 45 > 56 or 35 <= 45
print(b)
c= not(True)
print(c)
'''

#identify operators --> check for identity of an object --> id()

a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)



































































