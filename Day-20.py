'''
Functions --> Arguments Usage (varible length Arguments)
          --> Keyword variable length arguments (**kwargs)
Exception Handling/scope length of variables/Built-in functions

Exception handing -->It is a mechanism that helps to respond or make the flow of execution in normal way,
without this error will ocur

common Exceptions --> value Error,TypeError,IndexError,AttributeError ZeroDivisionError.....

Syntax:

try:
    #code that will cause the exception
except Exception aas e:
    #code will catch the exception
finally:
    #runs irrespective of try/except...
    .....
'''
'''
#basic Exception handling
try:
    #a=10
    a=int(input("enter the value"))
    #a== int or a==float
    result=20/a
    print(result)
#except Exception as e:
    #print(e)  #it returns the msg of error
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of variable properly')
    
#similarly if we want to check other Errors-->IndexError,AttributeError
#Multiple Exception Handling
    
try:
    a=[10,20,30]
    print(a[5])
#except Exception as e:
    #print(e)
except IndexError:
    print(f'Check the length of list properly and access elements')
except AttributeError:
    print(f'dont rush write the name properly')
'''

'''
def sample(*a,**b):
    """Usage of both Variable length and keyword variable length argument"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23")
'''
'''
try:
    a=[10,20,30]
    a.append(24)
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a=list(map(int,input("Enter").split(',')))
    print(a)
'''
'''

#BMI ---> bmi=(weight)/((height)**2)
#Feet --> 12inches-->1 inch --> 2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        #Write my logical condition
        if weight > 0 and height > 0:
            #continue
            break
            #print("bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print(f'Make sure to enter weight as integer only,height also as number')
bmi=((weight)/(height)**2)
print(bmi)


#scope of variables ---> scope is basically the region/area where it is accessible
#local scope,gobal,scope
#Global keyword,enclosing scope(Nested Functions non local keyword)
'''
'''
#local scope -->variables defined inside the function accessible inside
'''
'''
def display():
    """Usage of Local Scope"""
    name="codegnan" #local Varible
    print(name)
display()
#print(name) #it raises NameError
'''
'''
#Global Scope(variables) -->Defined outside and can be accessible anywhere
#in the script

place= "Hyderabad"#global variable
def display():
    """Usage of Local Scope & Global variable"""
    name="codegnan" #local Varible
    print(name)
    print(f'{name} is in {place}')
display()
print(place)
'''
'''
#Modifying global variable inside the function and accessible outside the function
count = 20
def data():
    """Usage of global keyword"""
    global count
    count = count+5
    print(f'value inside function is{count}')
data()
print(f'value outside function is {count}')
'''
'''
#local variable has high priority over global variable
count = 20
def data():
    """Proioroty of local vs global variable"""
    count=5
    count = count+5
    print(f'value inside function is{count}')
data()
print(f'value outside function is {count}')
'''
'''
#Enclosing Scope(nonlocal keyword)

def outer():
    """outer function with local variable"""
    count=5
    def inner():
        """Nested Function"""
        nonlocal count
        count =count+10
        print(f'value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()
'''
#built-in functions-->variales builtinScope
len=56
print(len+4)
print(len('codegnan'))



















    
