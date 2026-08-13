'''
Lists,Tuples...
'''
#Lists --> mutable,Ordered,Heterogenous

#index(),count(),copy(),sort(),reverse()
'''
details=['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('python'))#value Error

print(details.count(21))
print(details.count('python'))
'''
'''
data=['codegnan','sakesth','python','java']

for i in range (len(data)):
    print(i ,":",data[i])

for i in data:
    print(data.index(i) , ":" , i)
'''
#Copy()--> shallow copy of the given collection
'''
new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2]='Agentic Ai'
print(new)
print(data)

data.append('saketh')
print(data)
print(new)
'''
'''
data=[1,24,5,[21,31,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='agents'#in nested list the copy wont work 
print(new)
print(data)

new[1]='python'
print(new)
print(data)#mostly when we have nested list dont prefer copy()
'''
'''
marks=[14,24,-45,35,27]
print(marks)
#print(marks.sort())#returns none 
#print(marks)#returns in ascending order
#marks.sort(reverse = True )#returnd in descending order...
#print(marks)
marks.insert(2,'code')
#marks.sort() --> it cant sort as it includes string in list of int
#print(marks)

#reverse()-->returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])
'''

#type(),len(),min(),max(),print()
'''
print(sorted('codegnan'))#returms list in ascending order
'''
#print(sorted(['code','23',34,45]))#raises error

#tuple-->Tuples are Indexed,Ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notation
'''
a=()
print(type(a))
print(len(a))

dim=1.5,5.2
print(dim)
print(type(dim))
print(len(dim))
'''
#operations --> Indexing,slicing,striding,membership,merging,repetition
'''
courses=('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)

print(len(courses))

print(courses[3][7:])
#courses[2]=23 Tuples are Immutable
courses[-1].append('codegnan')#we can make any modifications inside list
print(courses)


#TASK:create a nested tuple as above work on slicing,striding and list fumc()

print('PFS' in courses)
d=courses*2#repetition
print(d)
e=courses + (2,3,4,5) #merging
print(e)

'''
#Tuples Immutable --> count(),Index()
'''
print(courses.index('JFS'))#returns first occurance
print(courses.count('agents'))

#print(courses.sort())#AttributeError-->sort() is in lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses))#as we have mixed type
      
#TypeCasting
d = tuple(sorted((23,13,4,11)))
print(d)
'''
'''
#accept group of integers space seperated
a,b=map(int,input("enter the values").split())
print(a,b)

a=tuple(map(int,input("enter:").split(',')))
print(a)
print('9+4')
#eval() func can take any kind of input
print(eval('9+4'))
'''

a=eval(input("enter:"))
print(a)
print(type(a))



































































