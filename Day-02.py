'''
Tokens ---> variables , puntuators

Variables --> Named memory location,its a placeholder for data
#Rules


#MultiAssignment of variables

name,place,age='nithish','hyd',22
print(name,place,age)
print(name,place,age,sep=',')
print(name,age,place,sep='----->')

#a,b=2,4,5 #Value error as too many values to unpack

name = 'code'
a,b = 4,1.3
print(a,b)
a,b = b,a
print(a,b,sep=',')

#a,b = b,c #nameError as c is not defined
#print(a,b)

#Deleting the variables -->del
#del a
#print (a)
#del a,b
#rint (a,b)

#Punctuators --> [](used for lists),{}(used for Dictionary,sets),()(used for tuples).
name = "codegnan" ; age = 7;course = 'DA'
print(name,age,course)

#DataTypes --> Numeric (int,float,complex),Boolean ,None,
            #--> Sequences -->Lists,Tuples,sets,strings,Frozensets,mapping(dict)
# in python spacing is called as intendation

#Numeric type -->int,float,complex

#int --> quantity,age....
age = 7
print(age)
print(type(age))

print(type(234))

#quantity = 02 #itis not allowed
#print (quantity)

#Float dataType --> temp,salary,price,average
price = 750.33 ; discount = 2.2
print(price,discount)
print(type(price))

#Complex --> its a combination of real and imaginary
i2 = 4
data = 5+i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True/False

valid = True
print(type(valid))

error = False
print(type(error))

#TYPE CASTING --> Converting one type to another type
#python by default follows Implicit type (we need not mention the datatype)
#we will go for explicit conversion
# Evry buildin data type is a built in function
#int,float,complex , bool

#typecasting --> int -->float,complex,bool
age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(0)
print(e)


#typecasting --> Float --> int,complex,bool
price = 35.5
print(type(price))
b = int(price)
print(b)
print(type(b))
c = complex(price)
print(c)
print(type(c))
d = bool(price)
print(d)
e = bool(0)
print(e)

#typecasting --> complex--> int,float,bool
data = 2+5j
print(type(data))
#b = int(data) #typeError
#print(b)
#print(type(b))
#c = complex(data)
#print(c)
#print(type(c))
d = bool(data)
print(d)
e = bool(0)
print(e)


e=int(float(bool(45))) # here first bool verify it as True(1) then float verify it as 1.0 then int verfiy as 1
print(e)
'''
f = 45+2.5+2+3j+False
print(f)

g= 34-2+3j*True
print(g)







