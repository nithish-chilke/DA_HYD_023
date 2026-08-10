'''
Strings--> CaseConversions,searching&Finding ,string testing methods,replace,space removal
'''
#Searching,Finding,replacing,Joining....
'''
a="Nithish"
print(len(a))
print(min(a))
print(max(a))

b=a.index ('N')#it returns the index position
print(b)
c=a.index('i')#it returns only firdt occurance
print(c)
d=a.index('i',3)#it returns the next occurance
print(d)

e=a.index('n',8)#it returns valueerror
print(e)
f=a.index('t')#it returns value error
print(f)

a="Nithish"
g=a.index('n',1,4)
print(g)

#rindex() --> returns last occurance
a="Codegnan"
b=a.rindex('g')
print(b)
b=a.rindex('n')#here 'n' is occuring at 7th index 
print(b)
#d=a.rindex('n',8)#it returns valueError
#print(d)

#count() --> returns the number of items object is repeating

print('Codegnan'.count('n'))
#print('code'.count(w))#it returns o as we dont have 'W' in code
print('cakshhaakshhak'.count('a'))


#Find()--> gives first occurance but it avoid error returns -1 if substring is not found
print('codegnan'.find('r'))#it returns -1

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))

a='Data'
print(len(a))
for i in a:
    print(a.count(i),a.index(i))

#Replacing,Splitting,Joining
#Strings are immutable
a='codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('Jhshdinkdbjanain#ndjjs'.replace('#',''))
print(a.replace('x','saketh'))#it returns same because no x term in a


#split()
a='code saketh python'
print(len(a))
b=a.split()
print(b)
print(len(b))
c='code,saketh,python'
d=c.split()
print(d)
print(len(d))
e=c.split(',')
print(e)
print(len(e))

#Join(iterable)-->concatenate any number of strings
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('saketh'))
print(' '.join('saketh'))
'''
#string testing method (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....
'''
a='codegnan13'
print(a.isalnum())#return True for alpha numeric
b='codegnan'
print(b.isalnum())
print(a.isalpha())#returns true for only alpha
print(a.isdigit())
print('2321'.isdigit())
print('2321'.isnumeric())
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
'''
'''
print('codegnan'.islower())#returns True for all lowercase
print('Codegnan'.isupper())#returns True for all uppercase
print('Codegnan Python'.istitle())
'''
#Space removal -->strip() (removes leading and trailing spaces)
'''
a='codegnan'
print(a.strip())
b=input("enter the string:").strip().lower()
print(b)
'''

#Zfill () filling with zeros as per given numeric string
print('12222'.zfill(8))

#center(),ljust(),rjust()---->alignment of strings
print('haii'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))










































































































